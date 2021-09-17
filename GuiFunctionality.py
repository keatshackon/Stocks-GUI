from GuiCoreFunctionality  import *
# from screen import *


# To Choose eithere Exchange A or B
def exchangesChoosen(a):
	if(a.get() == 1):
		print("Stock A Choosen")
		#You can write your Code here after commneting Above print statement
	elif(a.get() == 2):
		#You can write your Code here after commneting Above print statement
		print("Stock B Choosen")


# Execute when Fetch Cuurent price Button is Clicked
def FetchNewData(market_show_text):
	#write code 
	print("Fetching New Data...")
	cur_price = check_positions()
	market_show_text.config(text = str(cur_price))



def Fetch_Cur_Price():
	#returnn current market Price for the time being Suppose it is 60
	return 60

# After Selecting Sell Limit Order
def Sell_Calculation(cur_price,opt4,sell_limit_show_text):
	temp = opt_sell_limit_menu(opt4)
	sell_limit_show_text.config(text = str(cur_price - temp))
	SellLimit_Order(cur_price - temp);



# After Selecting Buy Limit Order
def Buy_Calculation(cur_price,opt3,buy_limit_show_text):
	temp = opt_buy_limit_menu(opt3)
	buy_limit_show_text.config(text = str(cur_price - temp))
	BuyLimit_Order(cur_price - temp);
	

def opt_sell_limit_menu(opt3):
	if(opt3.get == "1"):
		print(1)
		return 1
	elif(opt3.get() == "5"):
		print("5")
		return 5
	elif(opt3.get() == "10"):
		print("10")
		return 10
	elif(opt3.get() == "20"):
		print("20")
		return 20
	elif(opt3.get() == "25"):
		print("25")
		return 25
	elif(opt3.get() == "40"):
		print(40)
		return 40
	elif("No of Stocks"):
		print("0")
		return 0


def opt_buy_limit_menu(opt4):
	if(opt4.get == "1"):
		print(1)
		return 1
	elif(opt4.get() == "5"):
		print("5")
		return 5
	elif(opt4.get() == "10"):
		print("10")
		return 10
	elif(opt4.get() == "20"):
		print("20")
		return 20
	elif(opt4.get() == "25"):
		print("25")
		return 25
	elif(opt4.get() == "40"):
		print(40)
		return 40
	elif("No of Stocks"):
		print("0")
		return 0


# Executed when option selected from list 1 and submit nutton Clicked
def sub1(opt1):
	if(opt1.get() == "NY"):
		print("NY")
	elif(opt1.get() == "DY"):
		print("DY")
	elif(opt1.get() == "AY"):
		print("AY")
	elif(opt1.get() == "PY"):
		print("PY")
	else:
		print("Nothing Selected")



# Executed when option from list 2 selected and submit nutton Clicked
def sub2(opt2):
	if(opt2.get == "Cancel Order"):
		print("cancel")
		Cancel_Order()
	elif(opt2.get() == "Close Order"):
		print("Close")
		Close_order()
	elif(opt2.get() == "Stop Order"):
		print("Stop")
		Stop_Order()
	elif(opt2.get() == "Limit Order"):
		print("Limit")
		Limit_Order()
	else:
		print("Keats")


# According to requiremnt
def Cancel_Order():
	pass

def Close_order():
	pass

def Stop_Order():
	pass

def Limit_Order():
	pass


# stop Whole Application when Exit Button Clicked
def stopApp(root):
	root.destroy()

