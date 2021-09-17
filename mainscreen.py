from tkinter import *
from GuiFunctionality import *
from GuiCoreFunctionality  import *


w1=Tk()
w1.configure(background="#7E847F")
w1.title("Stocks Exchange")
w1.geometry("700x500+400+70")
w1.resizable(0, 0) 

var = IntVar()
R1 = Radiobutton(w1, text="Exchange A", variable = var, value = 1,command = lambda: exchangesChoosen(var))
R1.pack( anchor = W )
R2 = Radiobutton(w1, text="Exchange B", variable = var, value = 2,command = lambda: exchangesChoosen(var))
R2.pack( anchor = W )


market_label = Label(w1,text="Market Price",height=1,width=20,fg="#150401",bg="#0012FF")
market_label.pack()
market_label.place(x=150,y=100)

market_show_text =Label(w1,text = "30",height=1,width=15)
market_show_text.pack()
market_show_text.place(x=310,y=100)


market_fetch_btn=Button(w1,text="Fetch Current Price",height=1,width=20,bg="#0012FF",command = lambda:FetchNewData(market_show_text))
market_fetch_btn.pack()
market_fetch_btn.place(x=510,y=30)


buy_limit_btn=Button(w1,text="Buy Limit",height=1,width=20,bg="#00FF00",command = lambda:Buy_Calculation(Fetch_Cur_Price(),opt3,buy_limit_show_text))
buy_limit_btn.pack()
buy_limit_btn.place(x=150,y=150)


buy_limit_show_text=Label(w1,text = "0",height=1,width=15)
buy_limit_show_text.pack()
buy_limit_show_text.place(x=310,y=150)


sell_limit_btn=Button(w1,text="Sell Limit",height=1,width=20,bg="#FF0000",command = lambda:Sell_Calculation(Fetch_Cur_Price(),opt4,sell_limit_show_text))
sell_limit_btn.pack()
sell_limit_btn.place(x=150,y=200)

sell_limit_show_text=Label(w1,text = "0",height=1,width=15)
sell_limit_show_text.pack()
sell_limit_show_text.place(x=310,y=200)


exit_btn=Button(w1,text="Exit",height=2,width=15,bg="#FF0000",command=lambda:stopApp(w1))
exit_btn.pack()
exit_btn.place(x=35,y=440)

# Dropdown menu options
option1 = ["NY",
			"DY",
			"AY",
			"PY"]
  
# datatype of menu text
opt1 = StringVar()
  
# initial menu text
opt1.set( "Choose" )
  
# Create Dropdown menu
drop1 = OptionMenu( w1 , opt1 , *option1)
drop1.pack()
drop1.place(x = 150,y = 250)


submit1 = Button(w1,text="Submit",height=1,width=10,bg="#FFFFFF",command = lambda:sub1(opt1))
submit1.pack()
submit1.place(x=240,y=250)

# Dropdown menu options
option2 = ["Cancel Order",
			"Close Order",
			"Stop Order",
			"Limit Order"]
  
# datatype of menu text
opt2 = StringVar()
  
# initial menu text
opt2.set( "Choose" )
  
# Create Dropdown menu
drop2 = OptionMenu( w1 , opt2 , *option2 )
drop2.pack()
drop2.place(x=350,y=250)

submit2 = Button(w1,text="Submit",height=1,width=10,bg="#FFFFFF",command = lambda:sub2(opt2))
submit2.pack()
submit2.place(x=455,y=250)




option_no_stocks1 = ["1",
			"5",
			"10",
			"20",
			"25",
			"40"]
  
# datatype of menu text
opt3 = StringVar()
  
# initial menu text
opt3.set( "No of Stocks" )
  
# Create Dropdown menu
drop3 = OptionMenu( w1 , opt3 , *option_no_stocks1 )
drop3.pack()
drop3.place(x=450,y=150)



option_no_stocks2 = ["1",
			"5",
			"10",
			"20",
			"25",
			"40"]
  
# datatype of menu text
opt4 = StringVar()
  
# initial menu text
opt4.set( "No of Stocks" )
  
# Create Dropdown menu
drop4 = OptionMenu( w1 , opt4 , *option_no_stocks2 )
drop4.pack()
drop4.place(x=450,y=200)




w1.mainloop()