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
      201:'Created',
      202:'Accepted',
      204:'No content to be sent',
      206:'Partial Content',
      400:'Request error',
      401:'Unauthorized',
      409:'Conflict',
      500:'Server error'
    }
  #-----------------
  class assets:
  # Asset Settings
    class defaults:
      class profile:
        # This is where I am set setting default tags
        tags = ["User"]
        # This is the default pfp. ~~~ I am using a seprate file becouse of the base64 length
        pfp = 'default.pfp.png'
        # This is the default about me message
        about = "This is user doesn't have an about page yet"

  #-----------------
  class file:
  # File settings:
    dir = './' # For assets Ex: ./database/profiledata.json OR ./database/userdata.json
  #---------------
