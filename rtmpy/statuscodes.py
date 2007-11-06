# -*- encoding: utf8 -*-
#
# Copyright (c) 2007 The RTMPy Project. All rights reserved.
# 
# Arnar Birgisson
# Thijs Triemstra
# 
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""
Collection of commonly used constants with status codes.
"""

class StatusCodes:
    """
    Status codes for NetConnection, NetStream and SharedObject classes used in the Flash Player.
    
    """
    #: The NetConnection.call method was not able to invoke the server-side method or
    #: command.
    NC_CALL_FAILED = "NetConnection.Call.Failed"

    #: The URI specified in the NetConnection.connect method did not
    #: specify 'rtmp' as the protocol. 'rtmp' must be specified when connecting to
    #: a RTMP server. Either not supported version of AMF was used (3 when only 0 is supported).
    NC_CALL_BADVERSION = "NetConnection.Call.BadVersion"

    #: The application has been shut down (for example, if the application is out of
    #: memory resources and must shut down to prevent the server from crashing) or the server has shut down.
    NC_CONNECT_APPSHUTDOWN = "NetConnection.Connect.AppShutdown"

    #: The connection was closed successfully.
    NC_CONNECT_CLOSED = "NetConnection.Connect.Closed"

    #: The connection attempt failed.
    NC_CONNECT_FAILED = "NetConnection.Connect.Failed"

    #: The client does not have permission to connect to the application, the
    #: application expected different parameters from those that were passed,
    #: or the application name specified during the connection attempt was not found on
    #: the server.
    NC_CONNECT_REJECTED = "NetConnection.Connect.Rejected"

    #: The connection attempt succeeded.
    NC_CONNECT_SUCCESS = "NetConnection.Connect.Success"

    #: The application name specified during connect is invalid.
    NC_CONNECT_INVALID_APPLICATION = "NetConnection.Connect.InvalidApp"

    #: Invalid arguments were passed to a NetStream method.
    NS_INVALID_ARGUMENT = "NetStream.InvalidArg"

    # A recorded stream was deleted successfully.
    NS_CLEAR_SUCCESS = "NetStream.Clear.Success"

    #: A recorded stream failed to delete.
    NS_CLEAR_FAILED = "NetStream.Clear.Failed"

    #: An attempt to publish was successful.
    NS_PUBLISH_START = "NetStream.Publish.Start"

    #: An attempt was made to publish a stream that is already being published by someone else.
    NS_PUBLISH_BADNAME = "NetStream.Publish.BadName"
    
    #: An attempt to use a Stream method (at client-side) failed.
    NS_FAILED = "NetStream.Failed"
	
    #: An attempt to unpublish was successful.
    NS_UNPUBLISHED_SUCCESS = "NetStream.Unpublish.Success"
    
    #: Recording was started.
    NS_RECORD_START = "NetStream.Record.Start"

    #: An attempt was made to record a read-only stream.
    NS_RECORD_NOACCESS = "NetStream.Record.NoAccess"
    
    #: Recording was stopped.
    NS_RECORD_STOP = "NetStream.Record.Stop"

    #: An attempt to record a stream failed.
    NS_RECORD_FAILED = "NetStream.Record.Failed"

    #: Data is playing behind the normal speed.
    NS_PLAY_INSUFFICIENT_BW = "NetStream.Play.InsufficientBW"

    #: Playback was started.
    NS_PLAY_START = "NetStream.Play.Start"

    #: An attempt was made to play a stream that does not exist.
    NS_PLAY_STREAMNOTFOUND = "NetStream.Play.StreamNotFound"

    #: Playback was stopped.
    NS_PLAY_STOP = "NetStream.Play.Stop"

    #: An attempt to play back a stream failed.
    NS_PLAY_FAILED = "NetStream.Play.Failed"

    #: A playlist was reset.
    NS_PLAY_RESET = "NetStream.Play.Reset"

    #: The initial publish to a stream was successful. This message is sent to all subscribers.
    NS_PLAY_PUBLISHNOTIFY = "NetStream.Play.PublishNotify"
	
    # An unpublish from a stream was successful. This message is sent to all subscribers.
    NS_PLAY_UNPUBLISHNOTIFY = "NetStream.Play.UnpublishNotify"

    #: Playlist playback switched from one stream to another.
    NS_PLAY_SWITCH = "NetStream.Play.Switch"

    #: Playlist playback is complete.
    NS_PLAY_COMPLETE = "NetStream.Play.Complete"

    #: The subscriber has used the seek command to move to a particular location in the recorded stream.
    NS_SEEK_NOTIFY = "NetStream.Seek.Notify"

    #: The stream doesn't support seeking.
    NS_SEEK_FAILED = "NetStream.Seek.Failed"

    #: The subscriber has used the seek command to move to a particular location in the recorded stream.
    NS_PAUSE_NOTIFY = "NetStream.Pause.Notify"

    #: Publishing has stopped.
    NS_UNPAUSE_NOTIFY = "NetStream.Unpause.Notify"

    #: Unknown
    NS_DATA_START = "NetStream.Data.Start"
    
    #: The Python interpreter has encountered a runtime error. In addition to the standard infoObject
    #: properties, the following properties are set:
    #:
    #:  filename - name of the offending ASC file.
    #:  lineno - line number where the error occurred.
    #:  linebuf - source code of the offending line.
    APP_SCRIPT_ERROR = "Application.Script.Error"

    #: The Python interpreter has encountered a runtime warning. In addition to the standard infoObject
    #: properties, the following properties are set:
    #: 
    #:  filename - name of the offending ASC file.
    #:  lineno - line number where the error occurred.
    #:  linebuf - source code of the offending line.
    APP_SCRIPT_WARNING = "Application.Script.Warning"

    #: The Python interpreter is low on runtime memory. This provides an opportunity for the
    #: application instance to free some resources or take suitable action. If the application instance
    #: runs out of memory, it is unloaded and all users are disconnected. In this state, the server will
    #: not invoke the Application.onDisconnect event handler or the Application.onAppStop event handler.
    APP_RESOURCE_LOWMEMORY = "Application.Resource.LowMemory"

    #: This information object is passed to the onAppStop handler when the application is being shut down.
    APP_SHUTDOWN = "Application.Shutdown"

    #: This information object is passed to the onAppStop event handler when the application instance
    #: is about to be destroyed by the server.
    APP_GC = "Application.GC"

    #: Read access to a shared object was denied.
    SO_NO_READ_ACCESS = "SharedObject.NoReadAccess"

    #: Write access to a shared object was denied.
    SO_NO_WRITE_ACCESS = "SharedObject.NoWriteAccess"

    #: The creation of a shared object was denied.
    SO_CREATION_FAILED = "SharedObject.ObjectCreationFailed"

    #: The persistence parameter passed to SharedObject.getRemote() is different from the one used
    #: when the shared object was created.
    SO_PERSISTENCE_MISMATCH = "SharedObject.BadPersistence"
    
