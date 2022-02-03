from tkinter import *  
from functools import partial
top = Tk()
top.geometry("300x300") 
frame = Frame(top,bg = "yellow",width = 325,height = 300)
frame.grid(row = 0,column = 0,sticky = "NW")
frame.grid_propagate(0)
frame.update()
l_welcome = Label(frame,text = "Welcome to my Convertor",bg = "red")
l_welcome.place(x = 150, y = 150, anchor = "center")
l_result = Label(frame, text = "", bg = "white")



l_result["text"] = ""
l_value = Label(frame, text = "", bg = "blue")
e_value = Entry(top, textvariable="")

l_from = Label(frame, text = "Start unit", bg = "green")

    
selected_from = StringVar(top)
choices = []
from_opt = OptionMenu(frame, selected_from, choices)
from_opt.config(width = 8)


l_to = Label(frame, text = "", bg="green")
selected_to = StringVar(top)

to_opt = OptionMenu(frame, selected_to,choices)
to_opt.config(width = 8)
GO = Button(frame, text = "")


def convert(unit1Option,unit2Option,valueEntry,measurement):
  #functions
  unit1 = unit1Option.get()
  unit2 = unit2Option.get()
  value = valueEntry.get()
  ans = 0.0
  resultList=[]
  if value == "":
    l_result["text"] = "Please input a value"
    l_result.place(x = 70, y = 255)
    return
  value = float(value)
  # functions for converting with the same unit
  if unit1 == unit2:
    ans = float(value)
#All unit conversions
  if measurement == "Length":
    siValueList = [0.001,0.01,0.1,1000]
    unitList = ["millimeter","centimeter", "decimeter", "kilometer"]
    for i in range(len(siValueList)):
      formatted_value = "{:.3f}".format(value * siValueList[i])
      rslt = str(value) + " " + unitList[i] +'  ='+ str(formatted_value)+ " meter"
      resultList.append(rslt)
  elif measurement == "Temperature":
    siValueList = [273.15]
    unitList = ["celcius", "fahrenheit"]
    rslt = str(value)  +" "+ unitList[0] +'  ='+ str( "{:.2f}".format(value + siValueList[0]))+ " Kelvin"
    resultList.append(rslt)
    rslt = str(value) +" " +unitList[1] +'  ='+ str("{:.2f}".format((float(value) - 32) * 5 / 9 + siValueList[0]))+ " Kelvin"
    resultList.append(rslt)
  
  elif measurement == "Weight":
    unitList = ["tons", "pounds", "ounces", "grams"]
    siValueList = [1/907.185003, 1/0.4535925, 1/0.0283495, 1/1000]
    for i in range(len(siValueList)):
      formatted_value = "{:.4f}".format(value * siValueList[i])
      rslt = str(value) +" " +unitList[i] +'  ='+str(formatted_value)+ " kilograms"
      resultList.append(rslt)


#functions with centimeters
# functions for converting with centimeters and meters
  if unit1 == "centimeter" and unit2 == "meter":
      ans = float(value) / 100
  elif unit1 == "meter" and unit2 == "centimeter":
      ans = float(value) * 100

# functions for converting with centimeters and millimeters
  elif unit1 == "millimeter" and unit2 == "centimeter":
      ans = float(value) / 10
  elif unit1 == "centimeter" and unit2 == "millimeter":
      ans = float(value) * 10

# functions for converting with centimeters and decimeters
  elif unit1 == "centimeter" and unit2 == "decimeter":
      ans = float(value) / 10
  elif unit1 == "decimeter" and unit2 == "centimeter":
      ans = float(value) * 10

# functions for converting with centimeters and kilometers
  elif unit1 == "centimeter" and unit2 == "kilometer":
      ans = float(value) / 100000
  elif unit1 == "kilometer" and unit2 == "centimeter":
      ans = float(value) * 100000


# functions with meters
# functions for converting with meters and kilometers
  elif unit1 == "meter" and unit2 == "kilometer":
      ans = float(value) / 1000
  elif unit1 == "kilometer" and unit2 == "meter":
      ans = float(value) * 1000


# functions with decimeters
# functions for converting with decimeters and kilometers
  elif unit1 == "decimeter" and unit2 == "kilometer":
      ans = float(value) / 10000
  elif unit1 == "kilometer" and unit2 == "decimeter":
      ans = float(value) * 10000

# functions for converting with decimeters and meters
  elif unit1 == "decimeter" and unit2 == "meter":
      ans = float(value) / 10
  elif unit1 == "meter" and unit2 == "decimeter":
      ans = float(value) * 10



# functions with millimeters
# functions for converting with millimeters and kilometers
  elif unit1 == "millimeter" and unit2 == "kilometer":
      ans = float(value) / 1000000
  elif unit1 == "kilometer" and unit2 == "millimeter":
      ans = float(value) * 1000000
  
# functions for converting with millimeters and decimeters
  elif unit1 == "millimeter" and unit2 == "decimeter":
      ans = float(value) / 100
  elif unit1 == "decimeter" and unit2 == "millimeter":
      ans = float(value) * 100

# functions for converting with millimeters and meters
  elif unit1 == "millimeter" and unit2 == "meter":
      ans = float(value) / 1000
  elif unit1 == "meter" and unit2 == "millimeter":
      ans = float(value) * 1000
  

  # functions with tons
  # functions for converting with tons and pounds
  elif unit1 == "tons" and unit2 == "pounds":
      ans = float(value) * 2000
  elif unit1 == "pounds" and unit2 == "tons":
      ans = float(value) / 2000

  # functions for converting with tons and ounces
  elif unit1 == "tons" and unit2 == "ounces":
      ans = float(value) * 32000
  elif unit1 == "ounces" and unit2 == "tons":
      ans = float(value) / 32000

  # functions for converting with tons and grams
  elif unit1 == "tons" and unit2 == "grams":
      ans = float(value) * 907185
  elif unit1 == "grams" and unit2 == "tons":
      ans = float(value) / 907185

  # functions for converting with tons and kilograms
  elif unit1 == "tons" and unit2 == "kilograms":
      ans = float(value) * 907.1850030836
  elif unit1 == "kilograms" and unit2 == "tons":
      ans = float(value) / 907.185003

  # functions with pounds
  # functions for converting with pounds and ounces
  elif unit1 == "pounds" and unit2 == "ounces":
      ans = float(value) * 16
  elif unit1 == "ounces" and unit2 == "pounds":
      ans = float(value) / 16

  # functions for converting with pounds and grams
  elif unit1 == "pounds" and unit2 == "grams":
      ans = float(value) * 453.5925
  elif unit1 == "grams" and unit2 == "pounds":
      ans = float(value) / 453.5925

  # functions for converting with pounds and kilograms
  elif unit1 == "pounds" and unit2 == "kilograms":
      ans = float(value) * 0.4535925
  elif unit1 == "kilograms" and unit2 == "pounds":
      ans = float(value) / 0.4535925



  # functions with ounces
  # functions for converting with ounces and grams
  elif unit1 == "ounces" and unit2 == "grams":
      ans = float(value) * 28.3495
  elif unit1 == "grams" and unit2 == "ounces":
      ans = float(value) / 28.3495

  # functions for converting with ounces and kilograms
  elif unit1 == "ounces" and unit2 == "kilograms":
      ans = float(value) * 0.0283495
  elif unit1 == "kilograms" and unit2 == "ounces":
      ans = float(value) / 0.0283495
      
  # functions with grams
  # functions for converting with grams and kilograms
  elif unit1 == "grams" and unit2 == "kilograms":
      ans = float(value) / 1000
  elif unit1 == "kilograms" and unit2 == "grams":
      ans = float(value) * 1000

  # functions with celciustop.quit()
  # functions for converting with celcius and fahrenheit
  elif unit1 == "celcius" and unit2 == "fahrenheit":
      ans = (float(value) + 32) * 9 / 5
  elif unit1 == "fahrenheit" and unit2 == "celcius":
      ans = (float(value) - 32) * 5 / 9

  # functions for converting with centimeters and millimeters
  elif unit1 == "celcius" and unit2 == "kelvin":
      ans = float(value) + 273.15
  elif unit1 == "kelvin" and unit2 == "celcius":
      ans = float(value) - 273.15
  # functions with fahrenheit
  # functions for converting with fahrenheit and kelvin
  elif unit1 == "fahrenheit" and unit2 == "kelvin":
      ans = (float(value) - 32) * 5 / 9 + 273.15
  elif unit1 == "kelvin" and unit2 == "fahrenheit":
      ans = (float(value) + 32) * 9 / 5 - 273.15
  l_result["text"] = ans
  l_result.place(x = 180, y = 225)
  ydif = 0
  i=0
  panel = PanedWindow(frame,  height = 120, width = 300,orient=VERTICAL)
  si = Label(frame, text = "SI Unit", bg = "blue")
  panel.place(x = 20, y = 95)
  panel.add(si)
  for val in resultList:
    l_resultList= Label(frame, text = "", bg = "grey")
    l_resultList["text"] = val
    panel.add(l_resultList)
    
 
def showItems(measurement):
    choices = []
    if measurement =="Length":
      choices = ["millimeter","centimeter", "decimeter", "meter", "kilometer"]
    elif measurement =="Temperature":
      choices = ["kelvin","celcius", "fahrenheit"]
    elif measurement =="Weight":
      choices = ["tons", "pounds", "ounces", "grams", "kilograms"]
    l_welcome.config(text = "")
    l_welcome.config(bg = "yellow")
    l_result.config(bg = "yellow")
    l_result["text"] = ""
    l_value.config(text = "Input a value : ")
    l_value.config(bg = "orange")
    l_value.place(x = 5, y = 10)
    number1 = StringVar()
    e_value.config(bg="white")
    e_value.config(bd=2)
    e_value.config(textvariable=number1)
    e_value.place(x = 115, y = 10)
    
    l_from.config(text = "Start unit")
    l_from.config(bg = "green")
    l_from.place(x = 20, y = 40 )

    selected_from.set(choices[0])
    from_opt = OptionMenu(frame, selected_from, *choices)
    from_opt.config(width = 8)
    from_opt.place(x= 20, y = 65)
    
    l_to.config(text = "End unit")
    l_to.config(bg = "green")
    l_to.place(x = 180, y = 40 )
    selected_to = StringVar(top)
    selected_to.set(choices[0])
    
    to_opt = OptionMenu(frame, selected_to, *choices)
    to_opt.config(width = 8)
    to_opt.place(x= 180, y = 65)
    
    GO.config(bg="red")
    GO.config(bd=2)
    GO.config(text = "Result")
    GO.config(command = partial( convert,selected_from,selected_to,number1,measurement))
    GO.place(x = 100,y = 220)

menubar = Menu(top)
menubar.add_command(label = "Length", command = partial(showItems ,"Length"))
menubar.add_command(label = "Temperature", command = partial(showItems,"Temperature")) 
menubar.add_command(label = "Weight", command = partial(showItems, "Weight"))
# display the menu  
top.config(menu = menubar)  


top.mainloop()  
