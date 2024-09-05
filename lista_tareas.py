import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QListWidgetItem

class ListaTareas(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lista de Tareas")
        self.setGeometry(300, 300, 400, 300)
        self.setStyleSheet("rgb:192, 191, 188")

        self.layout = QVBoxLayout()

        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("Agregar nueva tarea...")
        self.layout.addWidget(self.task_input)

        self.add_task_button = QPushButton("Agregar tarea", self)
        self.add_task_button.clicked.connect(self.add_task)
        self.layout.addWidget(self.add_task_button)

        self.task_list = QListWidget(self)

        self.task_list.itemDoubleClicked.connect(self.mark_completed)

        self.layout.addWidget(self.task_list)
        self.delete_task_button = QPushButton("Eliminar tarea", self)
        self.delete_task_button.clicked.connect(self.delete_task)
        self.layout.addWidget(self.delete_task_button)

        self.setLayout(self.layout)

    def update_buttons(self):
        text = self.new_task_input.text()
        has_selection = bool(self.todo_list.selectedItems())
        self.add_task_button.setEnabled(bool(text))
        self.mark_done_button.setEnabled(has_selection)
        self.delete_task_button.setEnabled(has_selection)

    def add_task(self):
        task_text = self.task_input.text()
        if task_text:
            self.task_list.addItem(QListWidgetItem(task_text))
            self.task_input.clear()

    def delete_task(self):
        selected_items = self.task_list.selectedItems()
        if not selected_items: return
        for item in selected_items:
            self.task_list.takeItem(self.task_list.row(item))

    def mark_completed(self, item):
        if item:
            item.setText(f"[✓] {item.text()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    todo_app = ListaTareas()
    todo_app.show()
    sys.exit(app.exec_())
