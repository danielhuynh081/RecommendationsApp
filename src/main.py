###############################################################################
#
#       ************************************************************
#       ****            M A I N . P Y  ____  F I L E.           ****
#       ************************************************************
#
#
#     AUTHORS:      ╔══  GROUP #6  ═════════════════════════════╗
#                   ║                                           ║
#                   ║  Hemu Babis,         Elizabeth Barnett,   ║
#                   ║  Michael Bell,       Collin Bond,         ║
#                   ║  Daniel Huynh,       Q Ntsasa.            ║
#                   ╚═══════════════════════════════════════════╝
#
#   PROFESSOR:      Christopher Gilmore
#
#      COURSE:      CS-314 Elements of Software Engineering.
#
#       DATED:      Fall, 2024.
#
###############################################################################

import msvcrt
import sys
import textwrap  
from functions import activity_recommendation, food_recommendation, custom_recommendation  # Import functions
#   "main"
#
def main() -> int:
    # Welcome Menu
     print("Welcome to the AI Recommendation Software\nPress any key to continue")
     msvcrt.getch()
     while True:
    
        print("What type of recommendation would you like?\n(1) Activity Recommendation (2) Food recommendation (3) Custom Recommendation: ")
        key=msvcrt.getch()
        if key == b'1':
            activity=input("\nEneter location for Activity: ")
            # Activity Recommendation Function
            activity_recommendation(activity)
            break
        if key == b'2':
            food = input("\nEneter location for Food: ")
            # Food Recommendation Function
            food_recommendation(food)
            break
        if key == b'3':
            custom=input("\nWhat type of recommendation: ")
            # Custom Recommendation Function
            custom_recommendation(custom)
            break
        elif key == b'4':  # Exit option
            print("\nExiting the program...")
            sys.exit(0)  # Exit the program
            break
        else:
            print("\nInvalid choice. Please select 1, 2, 3, or 4.")
    
   
     return 0

    
###############################################################################

#   Hook for the "main" function...
#
if (__name__ == '__main__'):

    sys.exit( main() )






###############################################################################
###############################################################################
#   END.