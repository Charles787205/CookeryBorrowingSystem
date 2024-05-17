from .database import DatabaseModel
import shutil
import os
import datetime
class Item():

  def __init__(self, **kwargs):
    self.id = kwargs.get('id', None)
    self.quantity = kwargs.get('quantity', 0)
    self.price = kwargs.get('price', 0)
    self.name = kwargs.get('name', '')
    self.category = kwargs.get('category', '')
    self.image = kwargs.get('image', '')
    
  
  



  def save_image( file_path):
    # Check if the file is a picture
    if not Item.is_picture(file_path):
      raise ValueError("Invalid file format. Only pictures are allowed.")

    # Get the destination folder path
    destination_folder = 'images'

    # Generate the image name with the current date and time
    current_datetime = datetime.datetime.now()
    image_name = current_datetime.strftime("%Y%m%d%H%M%S") + os.path.splitext(file_path)[1]

    # Copy the file to the destination folder with the formatted image name
    shutil.copy(file_path, os.path.join(destination_folder, image_name))
    return image_name

  def is_picture(file_path):
    # Get the file extension
    file_extension = os.path.splitext(file_path)[1].lower()

    # Check if the file extension is a picture format
    picture_formats = ['.jpg', '.jpeg', '.png', '.gif']
    return file_extension in picture_formats

  @staticmethod
  def save_item(item):
    db = DatabaseModel().connect_db()
    cursor = db.cursor()
    sql = "INSERT INTO items (name, quantity, item_type,image) VALUES (%s, %s, %s,  %s)"
    val = (item.name, item.quantity, item.category, item.image)
    cursor.execute(sql, val)
    db.commit()
    db.close()
    return cursor.lastrowid
  

  @staticmethod
  def get_items_by_item_type(item_type):
    db = DatabaseModel().connect_db()
    cursor = db.cursor(dictionary=True)
    sql = "SELECT * FROM items WHERE item_type = %s"
    val = (item_type,)
    cursor.execute(sql, val)
    items = cursor.fetchall()
    db.close()
    return [Item(**item) for item in items]
  

  @staticmethod
  def get_item_by_id(item_id):
    db = DatabaseModel().connect_db()
    cursor = db.cursor(dictionary=True)
    sql = "SELECT * FROM items WHERE id = %s"
    val = (item_id,)
    cursor.execute(sql, val)
    item = cursor.fetchone()
    db.close()
    return Item(**item) if item else None
  

  @staticmethod
  def get_most_borrowed_items():
    db = DatabaseModel().connect_db()
    cursor = db.cursor(dictionary=True)
    sql = "SELECT item_id, SUM(quantity) as total_quantity FROM request_items GROUP BY item_id ORDER BY total_quantity DESC LIMIT 5"
    cursor.execute(sql)
    items = cursor.fetchall()
    db.close()

    new_items = [Item.get_item_by_id(item['item_id']) for item in items]
    return new_items
  
  
  @staticmethod 
  def get_borrowed_items_from_user_id(user_id):
    db = DatabaseModel().connect_db()
    cursor = db.cursor(dictionary=True)
    sql = "SELECT request_id, item.name, SUM(request_items.quantity) as quantity FROM request_items JOIN items as item ON item_id = item.id JOIN requests ON request_id = requests.id WHERE user_id = %s AND requests.status = 'approved' GROUP BY item_id;"

    values = (user_id,)
    cursor.execute(sql, values)
    results = cursor.fetchall()
    
    items = []
    for result in results:
      item = Item(name = result['name'], quantity = result['quantity'])
      items.append(item)
    return items