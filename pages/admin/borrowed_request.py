from PyQt5.QtWidgets import QFrame, QVBoxLayout, QScrollArea, QHBoxLayout, QPushButton, QLabel, QMessageBox
from models import Request
from .view_request import RequestView
class RequestsView(QFrame):


  def __init__(self, stacked_frame):
    super().__init__()
    self.stacked_frame = stacked_frame
    self.setup_ui()

  def setup_ui(self):
    
    self.setObjectName("RequestsView")
    self.requests_layout = QVBoxLayout(self)

    self.center_frame = QFrame()
    self.center_frame.setObjectName("requests_center_frame")
    self.center_layout = QVBoxLayout(self.center_frame)

    self.title = QLabel("Requests")
    self.title.setObjectName("title_label")

    self.label_frame = QFrame()
    self.label_frame.setObjectName("requests_label_frame")
    self.label_layout = QHBoxLayout(self.label_frame)

    self.request_id_label = QLabel("#")
    self.request_id_label.setObjectName("request_id_label")
    self.request_id_label.setFixedSize(200, 50)

    self.request_user_label = QLabel("User")
    self.request_user_label.setObjectName("request_user_label")
    self.request_user_label.setFixedSize(200, 50)

    self.status_label = QLabel("Status")
    self.status_label.setObjectName("request_status_label")
    self.status_label.setFixedSize(200, 50)

    self.request_date_label = QLabel("Date")
    self.request_date_label.setObjectName("request_date_label")
    self.request_date_label.setFixedSize(200, 50)

    self.label_layout.addWidget(self.request_id_label)
    self.label_layout.addWidget(self.request_user_label)
    self.label_layout.addWidget(self.status_label)
    self.label_layout.addWidget(self.request_date_label)

    self.scroll_area = QScrollArea()
    self.scroll_area.setObjectName("requests_scroll_area")
    self.scroll_area.setWidgetResizable(True)

    self.scroll_area_widget = QFrame()
    self.scroll_area_widget.setObjectName("requests_scroll_widget")
    self.scroll_area_layout = QVBoxLayout(self.scroll_area_widget)

    self.scroll_area_layout.addWidget(self.label_frame)

    requests = Request.get_requests()
    for request in requests:
      request_frame = self.add_request(request)
      self.scroll_area_layout.addWidget(request_frame)

    self.scroll_area_layout.addStretch()
    self.scroll_area.setWidget(self.scroll_area_widget)

    self.center_layout.addWidget(self.title)

    self.center_layout.addWidget(self.scroll_area)

    self.requests_layout.addWidget(self.center_frame)

    

    
  def add_request(self, request):
    request_frame = QFrame()
    request_frame_layout = QHBoxLayout(request_frame)
    request_frame.setObjectName("borrowed_request_frame")

    request_id_label = QLabel(str(request.id))
    request_id_label.setObjectName("request_id_label")
    request_id_label.setFixedSize(200, 50)

    request_user_label = QLabel(f"{request.user.first_name} {request.user.last_name}".title())
    request_user_label.setObjectName("request_user_label")
    request_user_label.setFixedSize(200, 50)

    request_status_label = QLabel(request.status)
    request_status_label.setObjectName("request_status_label")
    request_status_label.setFixedSize(200, 50)

    request_date_label = QLabel(str(request.created_at.strftime("%B %d, %Y")))
    request_date_label.setObjectName("request_date_label")
    request_date_label.setFixedSize(200, 50)


    request_frame_layout.addWidget(request_id_label)
    request_frame_layout.addWidget(request_user_label)
    request_frame_layout.addWidget(request_status_label)
    request_frame_layout.addWidget(request_date_label)

    
    request_frame.mousePressEvent = lambda event: self.view_request(request)
    return request_frame
  

  def view_request(self, request):
    view_request = RequestView(self.stacked_frame, request)
    self.stacked_frame.addWidget(view_request)
    self.stacked_frame.setCurrentWidget(view_request)
