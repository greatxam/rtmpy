# Copyright the RTMPy Project
#
# RTMPy is free software: you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 2.1 of the License, or (at your option)
# any later version.
#
# RTMPy is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with RTMPy.  If not, see <http://www.gnu.org/licenses/>.

"""
API for handling RTMP RPC calls.
"""

from zope.interface import implements
from twisted.internet import defer

from rtmpy import message



#: The id for an RPC call that does not require or expect a response.
NO_RESULT = 0
class BaseCallHandler(object):
    """
    Provides the ability to initiate, track and finish RPC calls. Each RPC call
    is given a unique id.

    Once a call is I{finished}, it is forgotten about. Call ids cannot be
    reused.

    @ivar _lastCallId: The value of the last initiated RPC call.
    @type _lastCallId: C{int}
    @ivar _activeCalls: A C{dict} of callId -> context. An active call has been
        I{initiated} but not yet I{finished}.
    """


    def __init__(self):
        self._lastCallId = 0
        self._activeCalls = {}


    def isCallActive(self, callId):
        """
        Whether the C{callId} is a valid identifier for a call awaiting a
        result.
        """
        return callId in self._activeCalls


    def getNextCallId(self):
        """
        Returns the next call id that will be returned by L{initiateCall}.

        This method is useful for unit testing.
        """
        return self._lastCallId + 1


    def getCallContext(self, callId):
        """
        Returns the context stored when L{initiateCall} was executed.

        If no active call is found, C{None} will be returned in its place.

        @param callId: The call id returned by the corresponding call to
            L{initiateCall}.
        @rtype: C{tuple} or C{None} if the call is not active.
        @note: Useful for unit testing.
        """
        return self._activeCalls.get(callId, None)


    def initiateCall(self, *args):
        """
        Starts an RPC call and stores any context for the call for later
        retrieval. The call will remain I{active} until L{finishCall} is called
        with the same C{callId}.

        @param args: The context to be stored whilst the call is active.
        @return: A id that uniquely identifies this call.
        @rtype: C{int}
        """
        callId = self._lastCallId = self.getNextCallId()

        self._activeCalls[callId] = args

        return callId


    def finishCall(self, callId):
        """
        Called to finish an active RPC call. The RPC call completed successfully
        (with some sort of response).

        @param callId: The call id returned by the corresponding call to
            L{initiateCall} that uniquely identifies the call.
        @return: The context with which this call was initiated or C{None} if no
            active call could be found.
        """
        return self._activeCalls.pop(callId, None)


    def discardCall(self, callId):
        """
        Called to discard an active RPC call. The RPC call was not completed
        successfully.

        The semantics of this method is different to L{finishCall}, it is useful
        for clearing up any active calls that failed for some arbitrary reason.

        @param callId: The call id returned by the corresponding call to
            L{initiateCall} that uniquely identifies the call.
        @return: The context with which this call was initiated or C{None} if no
            active call could be found.
        """
        return self._activeCalls.pop(callId, None)



class AbstractRemoteInvoker(BaseCallHandler):
    """
    Provides an API to make RPC calls and handle the response.
    """

    implements(message.IMessageSender)


    # IMessageSender
    def sendMessage(self, msg):
        """
        Sends a message. Must be implemented by subclasses.

        @param msg: L{message.IMessage}
        """
        raise NotImplementedError


    def callRemote(self, name, *args, **kwargs):
        """
        Builds and sends an RPC call to the receiving endpoint.

        This is a B{fire-and-forget} method, no result is expected or will be
        returned. If you expect a result from the receiving endpoint, use
        L{callRemoteWithResult}.

        @param name: The name of the method to invoke on the receiving endpoint.
        @type name: C{str}
        @param args: The list of arguments to be invoked on the remote method.
        @param kwargs['command']: The command arg to be sent as part of the RPC
            call. This should only be used in advanced cases and should
            generally be left alone unless you know what you're doing.
        @return: C{None}
        """
        command = kwargs.get('command', None)
        msg = message.Invoke(name, NO_RESULT, command, *args)

        self.sendMessage(msg)


    def callRemoteWithResult(self, name, *args, **kwargs):
        """
        Builds and sends an RPC call to the receiving endpoint and returns a
        L{defer.Deferred} that waits for a result. If an error notification is
        received then the C{errback} will be fired.

        @param name: The name of the method to invoke on the receiving endpoint.
        @type name: C{str}
        @param args: The list of arguments to be invoked.
        @param kwargs['command']: The command arg to be sent as part of the RPC
            call. This should only be used in advanced cases and should
            generally be left alone unless you know what you're doing.
        """
        command = kwargs.get('command', None)

        d = defer.Deferred()
        callId = self.initiateCall(d, name, args, command)
        m = message.Invoke(name, callId, command, *args)

        try:
            self.sendMessage(m)
        except:
            self.discardCall(callId)

            raise

        return d