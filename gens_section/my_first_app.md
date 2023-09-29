
# Useful information

The main modules for Qt are QtWidgets, QtGui and QtCore.

In Qt all top level widgets are windows -- that is, they don't have a parent and are not nested within another widget or layout. This means you can technically create a window using any widget you like.

What is a window? 
- Holds the user-interface of your application 
- Every application needs at least one (...but can have more)
- Application will (by default) exit when last window is closed

Widgets without a parent are invisible by default. So, after creating the window object, we must always call .show() to make it visible. You can remove the .show() and run the app, but you'll have no way to quit it!

## The Event Loop

The QApplication holds the event loop of the application — the core loop which governs all user interaction with the GUI.

Interaction with the application
- a press of a key, 
- click of a mouse, 
- or mouse movement

an event is placed on the event queue in the event loop.

queue is checked on each iteration and if a waiting event is found

the event and control is passed to the specific event handler for the event. 

The event handler deals with the event, then passes control back to the event loop to wait for more events





