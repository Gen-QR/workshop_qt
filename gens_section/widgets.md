# What's a Widget?

A widget is a component of the UI that the user can interact with

User interfaces are made up of multiple widgets, arranged within the window

# Let's have a quick look at some widgets

...

# Widgets continued

That's not even all the widgets! There's loads, see [the docs](https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/index.html#module-PySide2.QtWidgets)

## Important information
- Widgets come with their own set of methods and behaviours that can be modified as needed

# Let's get involved with some widgets
## ex_1.py
### QLables

QLabel is arguably the simplest widgets available in the Qt toolbox. 
- simple one-line piece of text that you can position in your application.

Open up `gens_section/ex_1.py`

and add the following to the `__init__` method of  the `MainWindow` class

```python
widget = QLabel("Hello")

self.setCentralWidget(widget)
```

run the file

WOW!

Now try adjusting the text size and alignment, add the following code between the two lines you just added

```python
    font = widget.font()
    font.setPointSize(30)
    widget.setFont(font)
    widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # the pipe here combines alignment flags
```

The alignment is specified by using a flag from the Qt. namespace. The flags available for horizontal alignment are:

| Flag	           | Behaviour                                    |
|-----------------|----------------------------------------------|
| Qt.AlignLeft	   | Aligns with the left edge.                   |
| Qt.AlignRight	  | Aligns with the right edge.                  |
| Qt.AlignHCenter	 | Centers horizontally in the available space. |
| Qt.AlignJustify	 | Justifies the text in the available space.   |
|Qt.AlignTop|	Aligns with the top.|
|Qt.AlignBottom|	Aligns with the bottom.|
|Qt.AlignVCenter|	Centers vertically in the available space.|
|Qt.AlignCenter|	Centers horizontally and vertically|

EVEN COOLER!

### QCheckbox

Replace `MainWindow` with this:

```python
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        widget = QCheckBox("This is a checkbox") # n.b.: we are instatiating the checkbox with a label, this isn't mandatory but it's handy
        widget.setCheckState(Qt.Checked)

        widget.stateChanged.connect(self.show_state)

        self.setCentralWidget(widget)


    def show_state(self, s):
        print(s == Qt.Checked)
        print(s) # n.b: current state number is displayed as an int with checked = 2, unchecked = 0, and partially checked = 1
```

run it and have a look

have a go at setting the checked state to partially checked

## QComboBox

Replace `MainWindow` with this:

```python
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        widget = QComboBox()
        widget.addItems(["One", "Two", "Three"])

        # The default signal from currentIndexChanged sends the index
        widget.currentIndexChanged.connect(self.index_changed)

        # The same signal can send a text string
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)


    def index_changed(self, i): # i is an int
        print(i)

    def text_changed(self, s): # s is a str
        print(s)
```

The .currentIndexChanged signal is triggered when the currently selected item is updated, by default passing the index of the selected item in the list. There is also a .currentTextChanged signal which instead provides the label of the currently selected item, which is often more useful.

Try adding the following, this allows users to enter values not currently in the list (they can be inserted or used as a value).

```python
widget.setEditable(True)
```

try modifying the behaviour of the insert

|Flag|	Behavior|
|-----|-----|
|QComboBox.NoInsert|	No insert|
|QComboBox.InsertAtTop|	Insert as first item|
|QComboBox.InsertAtCurrent|	Replace currently selected item|
|QComboBox.InsertAtBottom|	Insert after last item|
|QComboBox.InsertAfterCurrent|	Insert after current item|
|QComboBox.InsertBeforeCurrent|	Insert before current item|
|QComboBox.InsertAlphabetically|	Insert in alphabetical order|

```python
widget.setInsertPolicy(QComboBox.InsertAlphabetically)
```

## QLineEdit
A simple single line text editing box that users can type text into

Replace `MainWindow` with this:

```python
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        widget = QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText("Enter your text")

        #widget.setReadOnly(True) # uncomment this to make readonly

        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)

        self.setCentralWidget(widget)


    def return_pressed(self):
        print("Return pressed!")
        self.centralWidget().setText("BOOM!")

    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())

    def text_changed(self, s):
        print("Text changed...")
        print(s)

    def text_edited(self, s):
        print("Text edited...")
        print(s)
```

run it, type something and press enter. Look at the comand line

BOOM!

try adding the following, this defines which characters are valid and where

```python
widget.setInputMask('000.000.000.000;_')
```

# Section 1 Conclusion
- I hope you now know:
  - what Qt is
  - how to build and run a very simple app
  - what widgets are and have a general feel for how to manipulate thenm
