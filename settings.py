#-----------------------------------------------------------------------#
#                         --- Python Database ---
#
# Contributors: @Carter2565#5594, 
# This is the current database for PTSO-Exchange.
# This project can be used as a template for any python database.
#
#-----------------------------------------------------------------------#
class settings:
  class interface:
  # Interface Settings
    interface = True
  #-----------------
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
      401:'Unauthorized',
      409:'Conflict'
    }
  #-----------------
  class assets:
  # Asset Settings
    class defalts:
      class profile:
        # This is the default pfp. ~~~ I am using a seprate file becouse of the base64 length
        pfp = open(f"defaults/pfp.base64", "r").read()
        # This is the default about me message
        about = "This is user doesn't have an about page yet"

  #-----------------
  class file:
  # File settings:
    dir = './' # For assets Ex: ./database/profiledata.json OR ./database/userdata.json
  #---------------
