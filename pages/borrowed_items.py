from PyQt5.QtWidgets import QFrame, QVBoxLayout, QScrollArea, QHBoxLayout, QPushButton, QLabel, QMessageBox
from models import Item

class BorrowedItems(QFrame):

  def __init__(self, parent, user):
    super().__init__()
    self.user = user
    self.setup_ui()


  def setup_ui(self):
    self.setObjectName("BorrowedItems")
    self.borrowed_items_layout = QVBoxLayout(self)

    self.center_frame = QFrame()
    self.center_frame.setObjectName("borrowed_items_center_frame")
    self.center_layout = QVBoxLayout(self.center_frame)

    self.title = QLabel("Borrowed Items")
    self.title.setObjectName("title_label")

    self.label_frame = QFrame()
    self.label_frame.setObjectName("borrowed_items_label_frame")
    self.label_layout = QHBoxLayout(self.label_frame)

    self.item_id_label = QLabel("#")
    self.item_id_label.setObjectName("item_id_label")
    self.item_id_label.setFixedSize(200, 50)

    self.item_name_label = QLabel("Item")
    self.item_name_label.setObjectName("item_name_label")
    self.item_name_label.setFixedSize(200, 50)

    self.quantity_label = QLabel("Quantity")
    self.quantity_label.setObjectName("quantity_label")
    self.quantity_label.setFixedSize(200, 50)

 
    self.label_layout.addWidget(self.item_id_label)
    self.label_layout.addWidget(self.item_name_label)
    self.label_layout.addWidget(self.quantity_label)
   

    self.scroll_area = QScrollArea()
    self.scroll_area.setObjectName("borrowed_items_scroll_area")
    self.scroll_area.setWidgetResizable(True)

    self.scroll_area_widget = QFrame()
    self.scroll_area_widget.setObjectName("borrowed_items_scroll_widget")
    self.scroll_area_layout = QVBoxLayout(self.scroll_area_widget)

    self.scroll_area_layout.addWidget(self.label_frame)



    items = Item.get_borrowed_items_from_user_id(self.user.id)
    for index, item in enumerate(items,1):
      item_frame = self.add_borrowed_item(item, index)
      self.scroll_area_layout.addWidget(item_frame)

    self.scroll_area_layout.addStretch()
    self.scroll_area.setWidget(self.scroll_area_widget)

    self.center_layout.addWidget(self.title)
    self.center_layout.addWidget(self.scroll_area)

    self.borrowed_items_layout.addWidget(self.center_frame)

  def add_borrowed_item(self, item, index):
    item_frame = QFrame()
    item_frame.setObjectName("item_frame")
    item_layout = QHBoxLayout(item_frame)

    item_id = QLabel(str(index))
    item_id.setObjectName("item_id")
    item_id.setFixedSize(200, 50)

    item_name = QLabel(item.name)
    item_name.setObjectName("item_name")
    item_name.setFixedSize(200, 50)

    quantity = QLabel(str(item.quantity))
    quantity.setObjectName("quantity")
    quantity.setFixedSize(200, 50)


    item_layout.addWidget(item_id)
    item_layout.addWidget(item_name)
    item_layout.addWidget(quantity)
    

    return item_frame
  
  