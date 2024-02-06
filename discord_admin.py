from user import User
from privileges_admin import Privileges, Admin 

discord_admin = Admin('Jack', 'Sparrow', 'piratelife22',) # use Admin class as it inherits User
discord_admin.describe_user()
discord_admin.privileges.show_privileges()
