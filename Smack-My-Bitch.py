import  pyautogui,time
start = input("Do you want to start bombing now ? : ")
if start == "y" or start == "Y":
   time.sleep(3)
   i = 0
   while(True):
       if(i >= 20):
         pyautogui.typewrite("test") # write what you want to send here
         pyautogui.press("enter")
         time.sleep(30)
       else:
           pyautogui.typewrite("test") # write what you want to send here
           pyautogui.press("enter")
           i +=1  
else:
    print("Ok goodbye! ")
