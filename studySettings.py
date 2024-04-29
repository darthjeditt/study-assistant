# Here's the code for a StudySettingsDialog using PySide6. This dialog will allow users to add new study items
# to the list as well as edit existing ones. For simplicity, the code assumes that the study items will be unique.


class StudySettingsDialog(QDialog):
    def __init__(self, study_items, parent=None):
        super().__init__(parent)
        self.study_items = study_items
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Edit Study List")
        self.layout = QVBoxLayout(self)

        # Label
        self.info_label = QLabel("Add or edit study items:")
        self.layout.addWidget(self.info_label)

        # List of study items
        self.study_list_widget = QListWidget(self)
        self.study_list_widget.addItems(self.study_items)
        self.layout.addWidget(self.study_list_widget)

        # Line edit and button for adding new items
        self.item_input = QLineEdit(self)
        self.layout.addWidget(self.item_input)
        self.add_button = QPushButton("Add", self)
        self.layout.addWidget(self.add_button)

        # Button to save changes
        self.save_button = QPushButton("Save Changes", self)
        self.layout.addWidget(self.save_button)

        # Button actions
        self.add_button.clicked.connect(self.add_item)
        self.save_button.clicked.connect(self.accept)
        self.study_list_widget.itemDoubleClicked.connect(self.edit_item)

        self.setLayout(self.layout)

    def add_item(self):
        item_text = self.item_input.text()
        if item_text and item_text not in self.study_items:
            self.study_list_widget.addItem(item_text)
            self.item_input.clear()
        else:
            self.info_label.setText("Please enter a unique, non-empty item.")

    def edit_item(self, item):
        # When an item is double-clicked, set it to be editable
        item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)

    def get_study_items(self):
        # Retrieve the list of items from the QListWidget
        items = []
        for index in range(self.study_list_widget.count()):
            items.append(self.study_list_widget.item(index).text())
        return items


# This StudySettingsDialog class would be instantiated from within the MainWindow class.
# After the dialog is closed, the get_study_items method can be used to retrieve the updated list of study items.
# The MainWindow class would then need to use this updated list to refresh the studyList QListWidget.

# In the MainWindow, you would create and show this dialog like this:
# dialog = StudySettingsDialog(self.study_items, self)
# if dialog.exec():
#     self.study_items = dialog.get_study_items()
#     self.refresh_study_list()

# The MainWindow class would also contain the refresh_study_list method to update the QListWidget with new items.
# Note: Actual implementation would also include error handling and might allow for the deletion of items.
