########################################################################
# COMPONENT:
#    CONTROL
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary: 
#    This class stores the notion of Bell-LaPadula
########################################################################

# you may need to put something here...

from enum import Enum

class Control(Enum):
    # <<<<<<< HEAD

    clearance_levels = {

        "Public" : 0,
        "Confidential" : 1,
        "Privileged" : 2,
        "Secret" : 3
    }
    
    # def authenticate(username)->bool:
    #     pass
    # def securityConditionWrite():
    #     pass
    # def securityConditionRead():
    #     pass
    # def secret():
    #     pass
    # def privileged():
    #     pass
    # def confidential():
    #     pass
    # def public():
    #     pass
# =======
#     PUBLIC = 0
#     CONFIDENTIAL = 1
#     PRIVILEGED = 2
#     SECRET = 3
# >>>>>>> 9329eba12131d4f423938526e21fe1c394e89f63
