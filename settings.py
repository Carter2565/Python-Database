class settings:
  class server:
  # Database Server settings:
    ip = 'localhost'
    port = 8000
  #-----------------
  class error:
  # Error settings
    codes = {
      200:'Ok',
      202:'Accepted',
      204:'No content to be sent',
      400:'Request error',
      401:'Unauthorized'
    }
  #-----------------
  class assets:
  # Asset Settings
    page = 3 #length of asset pages
  #-----------------
  class file:
  # File settings:
    dir = './' # For assets Ex: ./database/profiledata.json OR ./database/userdata.json
  #---------------