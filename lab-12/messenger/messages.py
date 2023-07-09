########################################################################
# COMPONENT:
#    MESSAGES
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary: 
#    This class stores the notion of a collection of messages
########################################################################

# ADD CONTROL STUFFS IN THIS FILE!!!!!!
import control, message

##################################################
# MESSAGES
# The collection of high-tech messages
##################################################
class Messages:
    
    message_access_level = {
        "Public" : control.Control.PUBLIC,
        "Confidential" : control.Control.CONFIDENTIAL,
        "Privileged" : control.Control.PRIVILEGED,
        "Secret" : control.Control.SECRET
    }


    def security_condition_write(self, subject_control:int, asset_control:int)->bool:
        return subject_control <= asset_control

    def security_condition_read(self, subject_control:int, asset_control:int)->bool:
        return subject_control >= asset_control

    ##################################################
    # MESSAGES CONSTRUCTOR
    # Read a file to fill the messages
    ##################################################
    def __init__(self, filename):
        self._messages = []
        self._read_messages(filename)
        

    ##################################################
    # MESSAGES :: DISPLAY --- Reference for read
    # Display the list of messages
    ################################################## 
    def display(self, user_control_level):
        for m in self._messages:
            if self.security_condition_read(user_control_level, m.text_control):
                m.display_properties()
            else:
                print("YOU DON'T HAVE CLEARANCE!")
    

    ##################################################
    # MESSAGES :: SHOW   # TODO: READ OPERATION -- debug
    # Show a single message
    ################################################## 
    def show(self, id, user_control_level):
        # for m in self._messages:
        #     if self.security_condition_read(user_control_level, m.text_control):
        #         m.display_properties()
        #     else:
        #         print("YOU DON'T HAVE CLEARANCE!")
        for m in self._messages:
            if m.get_id() == id:
                if self.security_condition_read(user_control_level, m.text_control):
                    m.display_text()
                    return True
                else:
                    print("YOU DON'T HAVE CLEARANCE!")
                return False
            
                

    ##################################################
    # MESSAGES :: UPDATE   # TODO: WRITE OPERATION -- debug
    # Update a single message
    
    
     ################################################## 
    # def update(self, id, text):
    #     for m in self._messages:
    #         if m.get_id() == id:
    #           if self.security_condition_write(user_control_level, m.text_control):
    #             m.update_text(text)
    ################################################## 
    def update(self, id, text, user_control_level):
        
        #text_control = self.message_access_level.get(text_control)
        #m = message.Message(id, text, text_control.value)
        
        for m in self._messages:
            if m.get_id() == id:
                if self.security_condition_write(user_control_level, m.text_control):
                    m.update_text(text)
                else:
                    print("YOU DON'T HAVE CLEARANCE!")
                

    ##################################################
    # MESSAGES :: REMOVE   # TODO: WRITE -- debug
    # Remove a single message
    ################################################## 
    def remove(self, id, user_control_level):
    
        # text_control = self.message_access_level.get(text_control)
        # m = message.Message(id, text_control.value)
        # # self._messages.append(m) -- see if needed
 
        for m in self._messages:
            if m.get_id() == id:
                if self.security_condition_write(user_control_level, m.text_control):
                    m.clear()
            else:
                print("YOU DON'T HAVE CLEARANCE!")

    ##################################################
    # MESSAGES :: ADD --- Reference for write methods.-- checked
    # Add a new message
    ################################################## 
    def add(self, text, author, date, text_control, user_control_level):
        # Assign asset's text_control using corresponding dictionary values.
        text_control = self.message_access_level.get(text_control)
        
        # user_control_level = self.access_levels.get()

        if self.security_condition_write(user_control_level, text_control.value):
            # Create new message, passing in all pertinent information
            m = message.Message(text, author, date, text_control.value)
            self._messages.append(m)
        else:
            print("YOU DON'T HAVE CLEARANCE!")
            

    ##################################################
    # MESSAGES :: READ MESSAGES
    # Read messages from a file
    ################################################## 
    def _read_messages(self, filename):
        try:
            with open(filename, "r") as f:
                for line in f:
                    text_control, author, date, text = line.split('|') # Since we are getting text_control
                    self.add(text.rstrip('\r\n'), author, date, text_control, user_control_level=0)

        except FileNotFoundError:
            print(f"ERROR! Unable to open file \"{filename}\"")
            return
