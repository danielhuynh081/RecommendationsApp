###############################################################################
#
#       ************************************************************
#       ****            M A I N . P Y  ____  F I L E.           ****
#       ************************************************************

###############################################################################
import msvcrt
import sys
from huggingface_hub import login
import torch
from functions import generate_prompt, test_model  # Import functions
#   "main"
#
def main() -> int:
    # Welcome Menu
     login("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")
     print("Welcome to the AI Recommendation Software\nPress any key to continue")
     msvcrt.getch()
    
    
       # print("What type of recommendation would you like?\n(1) Activity Recommendation (2) Food recommendation (3) Trip Planner (4) Custom Recommendation (5) Exit: ")
       # key=msvcrt.getch()
     
     test_model()

     print("\nModel test complete.\n")

     return 0
'''
        if key == b'1':
            activity=input("\nEneter location for Activity: ")
            # Activity Recommendation Function
            generate_prompt(1,activity)
            break
        if key == b'2':
            food = input("\nEneter location for Food: ")
            # Food Recommendation Function
            generate_prompt(2,food)
            break
        if key == b'3':
            custom=input("\nWhere will you be traveling?: ")
            # Custom Recommendation Function
            generate_prompt(3,custom)
            break
        if key == b'4':
            custom=input("\nWhat recommendation would you like?: ")
            # Custom Recommendation Function
            generate_prompt(4,custom)
            break
        elif key == b'4':  # Exit option
            print("\nExiting the program...")
            sys.exit(0)  # Exit the program
            break
        else:
            print("\nInvalid choice. Please select 1, 2, 3, or 4.")
    
'''

    
###############################################################################

#   Hook for the "main" function...
#
if (__name__ == '__main__'):

    sys.exit( main() )






###############################################################################
###############################################################################
#   END.