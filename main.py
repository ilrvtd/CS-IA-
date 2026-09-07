import sqlite3
from tkinter import ttk
from tkinter import W, CENTER
import customtkinter
import select
import tkcalendar
from customtkinter import *
from CoreSystem import *
from CoreSystem import CoreSystem
from ProductManagement import *
from CTkMessagebox import CTkMessagebox
from tkinter import messagebox
from tkcalendar import Calendar




# creating the window with the size of the window, and letting user resize it.
app = CTk()
app.title("Product Flux")
app.geometry("1000x700")
app.resizable(True, True)

#I have to create an object of coresystem because I need to integrate the back end to the front end.
system = CoreSystem()

#creating frames to make the later process cleaner. CTk Frame is a frame creating function. Pack fill is organizing it.
#fill just fill the frame to the entire screen when it = both. Expand true. Pack basically makes all of ts visible.
#expand is basically like, if there is extra space around that area specified, can it fill it or nah

#all the frames

home_frame = CTkFrame(app)
product_management_frame = CTkFrame(app)
sales_management_frame = CTkFrame(app)
analytics_frame = CTkFrame(app)
suggestions_frame = CTkFrame(app)

#placing all the frames
home_frame.place(
    relx=0,
    rely=0,
    relwidth=1,
    relheight=1,
)

product_management_frame.place(
    relx=0,
    rely=0,
    relwidth=1,
    relheight=1,
)

sales_management_frame.place(
    relx=0,
    rely=0,
    relwidth=1,
    relheight=1,
)

analytics_frame.place(
    relx=0,
    rely=0,
    relwidth=1,
    relheight=1,
)

suggestions_frame.place(
    relx=0,
    rely=0,
    relwidth=1,
    relheight=1,
)

#i need frames for all the pages I have within this frame. So i added all of these frames for the respective pages

add_product_frame = CTkFrame(app, fg_color= "transparent")
view_product_frame = CTkFrame(app,fg_color= "transparent")
update_product_frame = CTkFrame(app, fg_color="transparent")
delete_product_frame = CTkFrame(app, fg_color="transparent")

add_product_frame.place(
                        relx=0,
                        rely=0,
                        relwidth=1,
                        relheight=1)
view_product_frame.place(
                            relx=0,
                            rely=0,
                            relwidth=1,
                            relheight=1)
update_product_frame.place(
                            relx=0,
                            rely=0,
                            relwidth=1,
                            relheight=1)

delete_product_frame.place(
                            relx=0,
                            rely=0,
                            relwidth=1,
                            relheight=1)

# these are the frames for creating pages in the sales management thing
add_sales_record_frame = CTkFrame(app, fg_color= "transparent")
view_sales_record_frame = CTkFrame(app,fg_color= "transparent")
update_sales_record_frame = CTkFrame(app, fg_color="transparent")
delete_sales_record_frame = CTkFrame(app, fg_color="transparent")

# i am placing the sales management frames here

add_sales_record_frame.place(
                        relx=0,
                        rely=0,
                        relwidth=1,
                        relheight=1)

view_sales_record_frame.place(
                            relx=0,
                            rely=0,
                            relwidth=1,
                            relheight=1)

update_sales_record_frame.place(
                            relx=0,
                            rely=0,
                            relwidth=1,
                            relheight=1)

delete_sales_record_frame.place(
                            relx=0,
                            rely=0,
                            relwidth=1,
                            relheight=1)

#i need frames for the analytics. I need an overview frame and a product performance frame

overview_frame_analytics_frame = CTkFrame(app, fg_color= "transparent")
product_performance_analytics_frame = CTkFrame(app, fg_color= "transparent")

overview_frame_analytics_frame.place(
                            relx=0,
                            rely=0,
                            relwidth=1,
                            relheight=1)

product_performance_analytics_frame.place(
                            relx=0,
                            rely=0,
                            relwidth=1,
                            relheight=1)

#I need to make frames for the suggestions thing as well here.

#initially making  home frame be on top
home_frame.tkraise()


#title for the home frame, after label, when specified, it says this title belongs to home_frame. Font and text size
#self-explanatory
title = CTkLabel(home_frame,text="Product Flux " , font =("Proxima Nova", 36))
title.pack(pady=50)


#now I want to give a subtitle to the main title and i also need to display it.
sub_title = CTkLabel(home_frame, text = " Inventory Management System and Product Performance Analysis",
                     font =("Arial", 20, "italic"))
sub_title.pack(pady=(0,25))

#now I have to build the buttons and functions
# this function basically goes back to home frame
def go_back_to_home_function():
    home_frame.tkraise()


# this function basically, upon clicking the product management button, it sends the product frame up
def open_product_management():
    product_management_frame.tkraise()


#product management
product_management_button = CTkButton(home_frame,
                                      command = open_product_management,
                                      text = "Product Management",
                                      width = 250,
                                      height = 50,
                                      font =("Arial", 20))

product_management_button.pack(pady=(0,10))


#product_management inside frame stuff

product_management_title = CTkLabel(product_management_frame,text = "Product Management" , font =("Arial", 30))

product_management_title.place(
                                relx=0.0001,
                                rely=0.1,
                                relwidth=0.5,
                                relheight=0.1)

product_management_close_button = CTkButton(product_management_frame,
                                            command= go_back_to_home_function ,
                                            text = "Back",
                                            width = 155,
                                            height = 30,
                                            font =("Arial", 17))

product_management_close_button.place(
                                            relx=0.8,
                                            rely=0.8,
                                            relwidth=0.08,
                                            relheight=0.07)

back_to_product_management_button = CTkButton( add_product_frame,
                                            command = open_product_management,
                                            text = "Back",
                                            width = 155,
                                            height = 30,
                                            font =("Arial", 17))

back_to_product_management_button.place(
                                            relx=0.8,
                                            rely=0.8,
                                            relwidth=0.08,
                                            relheight=0.06)


#i need buttons within the frame, for each function of the app for a product. So i am making these buttons.
#i will use another frame for the buttons to place them neatly and make it easier to work with.
button_container_product_management = CTkFrame(product_management_frame,fg_color="transparent")
button_container_product_management.place(
                        relx=0.15,
                        rely=0.3,
                        relwidth=0.17,
                        relheight=0.4)

#for every option within the product management section, I need another frame since its a new page in itself.
#so ill make frames for all of these buttons making it easier later on.


def open_add_product_frame():
    add_product_frame.tkraise()


def open_view_product_frame():
    view_product_frame.tkraise()


def open_update_product_frame():
    update_product_frame.tkraise()


def open_delete_product_frame():
    delete_product_frame.tkraise()


product_management_add_product_button = CTkButton(button_container_product_management,
                                                  command = open_add_product_frame,
                                                  text = " Add Product",
                                                  width = 200,
                                                  height = 45,
                                                  font = ("Arial", 20))

product_management_view_product_button = CTkButton(button_container_product_management,
                                                          command = open_view_product_frame,
                                                          text = "View Product",
                                                          width=200,
                                                          height=45,
                                                          font=("Arial", 20))

product_management_update_product_button = CTkButton(button_container_product_management,
                                                            command = open_update_product_frame,
                                                            text = "Update Product",
                                                            width = 200,
                                                            height = 45,
                                                            font = ("Arial", 20))

product_management_delete_product_button = CTkButton(button_container_product_management,
                                             command = open_delete_product_frame,
                                             text= " Delete Product",
                                             width = 200,
                                             height = 45,
                                             font = ("Arial", 20))

product_management_add_product_button.pack(pady = (0,10))
product_management_view_product_button.pack(pady = (0,10))
product_management_update_product_button.pack(pady=(0,10))
product_management_delete_product_button.pack(pady = (0,10))

# i will write the code for the add product page now.

add_product_title = CTkLabel(add_product_frame,text = "Add New Product " , font =("Arial", 30))
add_product_title.place(
                                relx=0.0001,
                                rely=0.1,
                                relwidth=0.5,
                                relheight=0.1)


#backend integration for add product page. I have to reword or slightly change the code a bit here in the core system
#and then i think i can use it here because that was for console stuff and i tested that and it worked.
# add product button backend integration function is here and i have to change the code in coresystem as well


#basically i found this other logical bug in my GUI thing. Basically the combobox list doesnt update immediately when im continously using the app. So i have to fix that.
# i will do that by creating this new function, where I can just continously referesh the list after the function has been called
# ill use this newlist as a referesh acting thing by continously confiuguring it again and again so it will referesh.


def refresh_products_list ():
    new_list = system.get_all_product_names()
    product_name_select_2_combobox.configure(values = new_list)
    product_name_select_combobox.configure(values= new_list)
    product_name_select_3_combobox.configure(values = new_list)



def add_product_finish_button():
    name = None
    selling_price = None
    cost = None

    #im using valid = true as like a security check thing so the function doesnt call the coresystem one when the thing is wrong
    valid = True

    # I have to adjust the error label specifcally for the error type with the correct rely values.
    # the name entry place values is:              relx=0.145,
    #                                             rely=0.23,
    #                                             relwidth=0.2,
    #                                             relheight=0.06

    # the price place entry values are:                  relx=0.17,
    #                                             rely=0.48,
    #                                             relwidth=0.15,
    #                                             relheight=0.06

    # the cost entry place entry values are :            relx=0.16,
    #                                             rely=0.59,
    #                                             relwidth=0.17,
    #                                             relheight=0.06

    success_label = CTkLabel(add_product_frame,
                            text= " Product added successfully!",
                            text_color="green")

    #i created this function for the 3 second disappear thing, basically the widget exists but no text so it looks transparent
    def clear_success_label ():
        success_label.configure(text = "")

    # ill create another function for the 3 second disappear thing for error labels to keep it clean
    def clear_error_label ():
        error_label.configure(text= "")


    # i am using this error label as a standard, and i will configure the text and position based on the error type
    error_label = CTkLabel(add_product_frame,
                           text = "",
                           text_color= "red")

    error_label.place(                   relx=0.17,
                                         relwidth=0.18,
                                         relheight=0.06
                                         )


    # Name Validation
    if product_name_entry.get().strip() == "":

        # create the show error here, cannot be an empty text field.
        valid = False
        product_name_entry.focus()
        error_label.configure(text= "Product name cannot be empty")
        error_label.place_configure(           relx=0.145,
                                                 rely= 0.36,
                                                relwidth=0.22,
                                               relheight=0.06)
        error_label.after(3000, clear_error_label)
        return


    else:
        name = product_name_entry.get().strip()


    #Price Validation

    try:
        selling_price = float(product_price_entry.get())

        if selling_price <= 0:
            #show the enter a positive product price error message
            valid = False
            error_label.configure(text= "Product price cannot be negative")
            error_label.place_configure(        relx= 0.145,
                                                 rely=0.54,
                                                relwidth=0.2,
                                                 relheight=0.06)
            error_label.after(3000, clear_error_label)
            product_price_entry.focus()
            return

    except ValueError:

        #show the error message if user entered alphabets instead of numeric values
        valid = False
        error_label.configure(text=" Price cannot have alphabets or be empty")
        error_label.place_configure(relx=0.145,
                                    rely=0.54,
                                    relwidth=0.25,
                                    relheight=0.06)
        error_label.after(3000, clear_error_label)
        product_price_entry.focus()
        return


    #cost validation
    try:
        cost = float(product_cost_entry.get())

        if cost <= 0:

        # show the enter a positive product price error message
            valid = False
            error_label.configure(text=" Product cost cannot be negative")
            error_label.place_configure(relx=0.145,
                                    rely=0.72,
                                    relwidth=0.2,
                                    relheight=0.06)
            error_label.after(3000, clear_error_label)
            product_cost_entry.focus()
            return

    except ValueError:

        # show the error message if user entered alphabets instead of numeric values
        valid = False
        error_label.configure(text=" Cost cannot have alphabets or be empty")
        error_label.place_configure(relx=0.145,
                                    rely=0.72,
                                    relwidth=0.25,
                                    relheight=0.06)
        error_label.after(3000, clear_error_label)
        product_cost_entry.focus()
        return


    if valid:
        system.add_products(name,selling_price,cost)
        success_label.place(relx=0.33,
                           rely=0.8,
                           relwidth=0.18,
                           relheight=0.06)
        product_name_entry.delete(0,"end")
        product_price_entry.delete(0, "end")
        product_cost_entry.delete(0,"end")
        add_product_frame.after(3000, clear_success_label)
        refresh_products_list()




# i want to save the status label just in case i need it later on for some reason and the exact x and y values cuz
# im not figuring out the x and y value all that again🙏
#status_label = CTkLabel(add_product_frame,
                 #               text= " Product added successfully !",
                   #             text_color="green"
                   #             )

        #status_label.place(relx=0.31,
                      #     rely=0.8,
                        #   relwidth=0.16,
                          # relheight=0.06)


add_product_name_title = CTkLabel(add_product_frame, text= "Product Name ")

add_product_button = CTkButton(add_product_frame,
                               command= add_product_finish_button,
                               text = "Add Product" ,
                               width = 175,
                               height = 22,
                               font=("Arial",17 ) )

add_product_button.place(
                                            relx=0.18,
                                            rely=0.8,
                                            relwidth=0.13,
                                            relheight=0.06)

product_name_entry = CTkEntry(add_product_frame)



product_name_entry.place(                     relx=0.17,
                                            rely=0.3,
                                            relwidth=0.15,
                                            relheight=0.06)

product_name_entry_label = CTkLabel(add_product_frame,
                                    text="Product Name",
                                    font= ("Arial",20))

product_name_entry_label.place(             relx=0.145,
                                            rely=0.23,
                                            relwidth=0.2,
                                            relheight=0.06)

product_price_entry = CTkEntry(add_product_frame)


product_price_entry.place(                  relx=0.17,
                                            rely=0.48,
                                            relwidth=0.15,
                                            relheight=0.06)

product_price_entry_label = CTkLabel(add_product_frame,
                                     text="Product Price",
                                     font=("Arial", 20))

product_price_entry_label.place(             relx=0.145,
                                            rely=0.41,
                                            relwidth=0.2,
                                            relheight=0.06)



product_cost_entry = CTkEntry(add_product_frame)

product_cost_entry.place(                  relx=0.17,
                                            rely=0.66,
                                            relwidth=0.15,
                                            relheight=0.06)
product_cost_entry_label = CTkLabel(add_product_frame,
                                    text="Product Cost",
                                    font=("Arial", 20))

product_cost_entry_label.place(             relx=0.16,
                                            rely=0.59,
                                            relwidth=0.17,
                                            relheight=0.06)


#update product details page

update_product_title = CTkLabel(update_product_frame,text = "Update Product Details" , font =("Arial", 30))
update_product_title.place(
                                relx=0.0001,
                                rely=0.1,
                                relwidth=0.5,
                                relheight=0.1)

back_to_product_management_button = CTkButton(update_product_frame,
                                              command= open_product_management,
                                              text = "Back",
                                              width = 155,
                                              height = 27,
                                              font = ("Arial", 17))

back_to_product_management_button.place(
                                            relx=0.8,
                                            rely=0.855,
                                            relwidth=0.08,
                                            relheight=0.06)

list_products = system.get_all_product_names()

product_name_select_3_combobox = CTkComboBox(update_product_frame, values = list_products,width=200,
                                            height = 41,)

product_name_select_3_combobox.set("")

product_name_select_3_combobox.place(       relx=0.16,
                                            rely=0.3)

product_name_select_3_label = CTkLabel(update_product_frame,
                                    text=" Select Product",
                                    font= ("Arial",22))

product_name_select_3_label.place(          relx=0.13,
                                            rely=0.23,
                                            relwidth=0.25,
                                            relheight=0.06)

# basically I need to display the current condition of the products , because this is more helpful for the user
# what i can do is create new widgets and display upon the name selection. When the name is selected, I can display it accordingly
# i cant use place forget when a product detial is update, so I have create the labels outside the function


#i am creating the main bigger labels here.
current_name_label = CTkLabel(update_product_frame,
                              text="Current Name: ",
                              font=("Arial", 20),
                              )

current_price_label = CTkLabel(update_product_frame,
                               text="Current Price: ",
                               font=("Arial", 20))

current_cost_label = CTkLabel(update_product_frame,
                              text="Current Cost: ",
                              font=("Arial", 20))


# i am making sub labels so ill place them next to the labels with a colon so it will look better .

current_name_sub_label = CTkLabel(update_product_frame,
                                  font=("Arial", 17))
current_price_sub_label = CTkLabel(update_product_frame,
                                   font=("Arial", 17))
current_cost_sub_label = CTkLabel(update_product_frame,
                                  font=("Arial", 17))



def display_current_values (sonion):


    #i am setting values here because i set combobox to empty over there and its creating a stupid bug
    current_name = product_name_select_3_combobox.get()
    current_price = system.get_product_price_by_name(current_name)
    current_cost = system.get_product_cost_by_name(current_name)

    #i will configure these values when the function is called so real-time values are there.
    current_name_sub_label.configure(text = current_name)
    current_price_sub_label.configure(text= str(current_price))
    current_cost_sub_label.configure(text= str(current_cost))

    update_product_frame.update_idletasks()


    current_name_label.place(               relx=0.4,
                                            rely=0.3,
                                            relwidth=0.25,
                                            relheight=0.06)

    current_name_sub_label.place(           relx=0.6,
                                            rely=0.3,
                                            relwidth = 0.2,
                                            relheight = 0.06)

    current_price_label.place(              relx=0.397,
                                            rely=0.4,
                                            relwidth=0.25,
                                            relheight=0.06)

    current_price_sub_label.place(          relx=0.6,
                                            rely=0.4,
                                            relwidth = 0.2,
                                            relheight = 0.06)

    current_cost_label.place(               relx=0.395,
                                            rely=0.5,
                                            relwidth=0.25,
                                            relheight=0.06)

    current_cost_sub_label.place(           relx=0.6 ,
                                            rely=0.5,
                                            relwidth=0.2,
                                            relheight=0.06)




product_name_select_3_combobox.configure(command = display_current_values)


# i am creating labels and entries that will adapt to the type of change so i can the GUI more clean
temp_entry = CTkEntry(update_product_frame)
temp_label = CTkLabel(update_product_frame)


list_of_change = ["Name", "Price", "Cost"]
select_change_combobox = CTkComboBox( update_product_frame,
                                     values=list_of_change,
                                     width=200,
                                     height=41)
select_change_combobox.place(relx=0.16,
                             rely=0.5)

select_change_combobox.set("")



#i need the 3 seconds disappear thing

def selection_widget_showup(son):

    temp_label.place(relx=0.14,
                     rely=0.625,
                     relwidth=0.25,
                     relheight=0.06)


    if select_change_combobox.get() == "Name":

        temp_label.configure(text=" Enter new product name",
                             font=("Arial", 22))


        temp_entry.place(relx=0.175,
                         rely=0.7,
                         relwidth=0.17,
                         relheight=0.06)

    elif select_change_combobox.get() == "Price" :

        temp_label.configure(text=" Enter new price",
                             font=("Arial", 22))
        temp_label.place_configure(relx = 0.132)

        temp_entry.place(relx=0.175,
                         rely=0.7,
                         relwidth=0.17,
                         relheight=0.06)

    elif select_change_combobox.get() == "Cost":
        temp_label.configure(text=" Enter new cost ",
                             font=("Arial", 22))

        temp_label.place_configure(relx=0.132)

        temp_entry.place(relx=0.175,
                         rely=0.7,
                         relwidth=0.17,
                         relheight=0.06)



select_change_combobox.configure(command = selection_widget_showup)



select_change_label = CTkLabel(update_product_frame,
                               text=" Select change type",
                               font=("Arial", 22))


select_change_label.place(                  relx=0.145,
                                            rely=0.43,
                                            relwidth=0.22,
                                            relheight=0.06)


def update_product_details_GUI ():

    name = product_name_select_3_combobox.get()



    success_label= CTkLabel(update_product_frame,
                              text="",
                              text_color="green")

    success_label.place(relx=0.35,
                         rely=0.845,
                         relwidth=0.2,
                         relheight=0.07)

    error_label = CTkLabel(update_product_frame,
                           text="",
                           text_color="red")

    error_label.place(relx=0.16,
                              rely=0.565,
                              relwidth=0.2,
                              relheight=0.07)

    def clear_success_label ():
        success_label.configure(text = "")

    def clear_error_label ():
        error_label.configure(text = "")


    if product_name_select_3_combobox.get() == "" :
        valid = False

        error_label.configure(text="Selection cannot be empty")
        error_label.place(relx=0.16,
                                    rely=0.37,
                                    relwidth=0.2,
                                    relheight=0.06)
        error_label.after(3000, clear_error_label)

        product_name_select_2_combobox.focus()
        return

    products_names = system.get_all_product_names()
    if product_name_select_3_combobox.get() not in products_names:

            valid = False
            error_label.configure(text=" Please select product from the list only")
            error_label.place(relx=0.137,
                              rely=0.37,
                              relwidth=0.25,
                              relheight=0.06)
            error_label.after(3000, clear_error_label)
            product_name_select_3_combobox.focus()
            return

    product_ID = system.get_product_ID_by_name(name)
    valid = True

    if select_change_combobox.get() == "":

        valid = False

        error_label.configure(text="Selection cannot be empty")
        error_label.place(relx=0.16,
                          rely=0.56,
                          relwidth=0.2,
                          relheight=0.06)
        error_label.after(3000, clear_error_label)
        return

        # i basically found this bug, where I can type into the combobox and bypass everything. So i need to validate it
    if select_change_combobox.get() not in list_of_change:
        valid = False

        error_label.configure(text="Select only the changes given in the list")
        error_label.place(relx=0.1372,
                          rely=0.56,
                          relwidth=0.25,
                          relheight=0.06)
        error_label.after(3000, clear_error_label)
        return


    # this is the entire thing for name change only
    if select_change_combobox.get() == "Name":
        name = product_name_select_3_combobox.get()
        new_name = temp_entry.get()
        product_ID = system.get_product_ID_by_name(name)
        valid = True

        if new_name.strip() == "":

            valid = False

            error_label.configure(text="Name cannot be empty")
            error_label.place(relx=0.16,
                              rely=0.76,
                              relwidth=0.2,
                              relheight=0.07)
            error_label.after(3000, clear_error_label)

        # i need to ensure that the same product name cannot be repeated so other bugs in the system wont be created.
        # because the user doesnt know what they meant, and system also gets confused and big mess.

        product_names = system.get_all_product_names()
        for i in range(0, len(product_names)):
            if new_name == product_names[i]:
                valid = False
                error_label.configure(text="New name already exists, choose another one")
                error_label.place(relx=0.115,
                                      rely=0.76,
                                      relwidth=0.32,
                                      relheight=0.06)
                error_label.after(3000, clear_error_label)

                temp_entry.focus()
                return


        if valid:
            system.database.update_product_name(product_ID,new_name)
            success_label.configure(text="Detail Updated Successfully!")
            success_label.after(3000, clear_success_label)
            product_name_select_3_combobox.set("")
            select_change_combobox.set("")
            temp_label.place_forget()
            temp_entry.place_forget()
            current_name_label.place_forget()
            current_price_label.place_forget()
            current_cost_label.place_forget()
            current_name_sub_label.place_forget()
            current_price_sub_label.place_forget()
            current_cost_sub_label.place_forget()
            refresh_products_list()
            temp_entry.delete(0,"end")

    #this only for price change
    if select_change_combobox.get() == "Price" :

        name = product_name_select_3_combobox.get()
        product_ID = system.get_product_ID_by_name(name)
        new_price = temp_entry.get()
        valid = True

        if  new_price == "":
            valid = False

            error_label.configure(text="Price cannot be empty")
            error_label.place(relx=0.16,
                              rely=0.76,
                              relwidth=0.2,
                              relheight=0.06)
            error_label.after(3000, clear_error_label)

            temp_entry.focus()
            return

        try:
            if float(new_price) <= 0 :
                valid = False

                error_label.configure(text="Price cannot be negative or zero")
                error_label.place(relx=0.16,
                                  rely=0.76,
                                  relwidth=0.2,
                                  relheight=0.06)
                error_label.after(3000, clear_error_label)

                temp_entry.focus()
                return

        except ValueError:

            valid = False

            error_label.configure(text="Price cannot have alphabets")
            error_label.place(relx=0.16,
                              rely=0.76,
                              relwidth=0.2,
                              relheight=0.06)
            error_label.after(3000, clear_error_label)

            temp_entry.focus()
            return

        if valid:
            system.database.update_product_selling_price(product_ID,new_price)
            success_label.configure(text="Detail Updated Successfully!")
            success_label.after(3000, clear_success_label)
            product_name_select_3_combobox.set("")
            select_change_combobox.set("")
            temp_label.place_forget()
            temp_entry.place_forget()
            current_name_label.place_forget()
            current_price_label.place_forget()
            current_cost_label.place_forget()
            current_name_sub_label.place_forget()
            current_price_sub_label.place_forget()
            current_cost_sub_label.place_forget()
            refresh_products_list()
            temp_entry.delete(0, "end")


    #this only for the cost change of a product
    if select_change_combobox.get() == "Cost" :

        name = product_name_select_3_combobox.get()
        product_ID = system.get_product_ID_by_name(name)
        new_cost = temp_entry.get()
        valid = True

        if  new_cost == "":
            valid = False

            error_label.configure(text="Cost cannot be empty")
            error_label.place(relx=0.16,
                              rely=0.73,
                              relwidth=0.2,
                              relheight=0.07)
            error_label.after(3000, clear_error_label)

            temp_entry.focus()
            return

        try:
            if float(new_cost) <= 0 :

                valid = False

                error_label.configure(text="Cost cannot be negative or zero")
                error_label.place(relx=0.16,
                                  rely=0.76,
                                  relwidth=0.2,
                                  relheight=0.06)
                error_label.after(3000, clear_error_label)

                temp_entry.focus()
                return

        except ValueError:

            valid = False

            error_label.configure(text="Cost cannot have alphabets")
            error_label.place(relx=0.16,
                              rely=0.76,
                              relwidth=0.2,
                              relheight=0.06)
            error_label.after(3000, clear_error_label)

            temp_entry.focus()
            return


        if valid:
            system.database.update_product_cost(product_ID,new_cost)
            success_label.configure(text = "Detail Updated Successfully!")
            success_label.after(3000, clear_success_label)
            product_name_select_3_combobox.set("")
            select_change_combobox.set("")
            temp_label.place_forget()
            temp_entry.place_forget()
            current_name_label.place_forget()
            current_price_label.place_forget()
            current_cost_label.place_forget()
            current_name_sub_label.place_forget()
            current_price_sub_label.place_forget()
            current_cost_sub_label.place_forget()
            refresh_products_list()
            temp_entry.delete(0, "end")




update_product_button = CTkButton(update_product_frame,
                               command= update_product_details_GUI,
                               text = "Update Details" ,
                               width = 175,
                               height = 22,
                               font=("Arial",17 ) )


update_product_button.place(
                                            relx=0.1925,
                                            rely=0.85,
                                            relwidth=0.13,
                                            relheight=0.06)






#delete product page
delete_product_title = CTkLabel(delete_product_frame,text = "Delete Products" , font =("Arial", 30))
delete_product_title.place(
                                relx=0.0001,
                                rely=0.1,
                                relwidth=0.5,
                                relheight=0.1)



#now ill write the code for the delete product page, because its easier and quick to finish.
# im making the product name select combobox thing so i can select product and stuff
list_products = system.get_all_product_names()

product_name_select_2_combobox = CTkComboBox(delete_product_frame, values = list_products,width=200,
                                            height = 41)
product_name_select_2_combobox.set("")

product_name_select_2_combobox.place(         relx=0.4,
                                            rely=0.43,
                                            )


def delete_selected_product ():

    product_name = product_name_select_2_combobox.get()
    product_ID = system.get_product_ID_by_name(product_name)
    valid = True

    success_label1 = CTkLabel(delete_product_frame,
                             text="",
                             text_color="green")

    success_label1.place(relx=0.39,
                        rely=0.62,
                        relwidth=0.2,
                        relheight=0.07)

    # im creating a sub function to call it when the button is clicked so 3 seconds later the label disappears.
    def clear_success_label():
        success_label1.configure(text="")

    def clear_error_label():
        error_label.configure(text="")


    error_label = CTkLabel(delete_product_frame,
                           text="",
                           text_color="red")


    if product_name.strip() == "":
        valid = False

        error_label.configure(text="Selection cannot be empty")
        error_label.place_configure(relx=0.39,
                                    rely=0.49,
                                    relwidth=0.2,
                                    relheight=0.07)
        error_label.after(3000, clear_error_label)

        product_name_select_2_combobox.focus()


    if valid:
        system.delete_product(product_ID)
        success_label1.configure(text = "Product Deleted Successfully")
        product_name_select_2_combobox.set("")
        success_label1.after(3000, clear_success_label)
        refresh_products_list()


delete_product_button = CTkButton(delete_product_frame,
                                  command = delete_selected_product,
                                  text = "Delete Product",
                                  width = 175,
                                  height = 22,
                                  font= ("Arial", 17)
                                  )


delete_product_button.place(
                                            relx=0.415,
                                            rely=0.56,
                                            relwidth=0.16,
                                            relheight=0.06)



product_name_select_label1 = CTkLabel(delete_product_frame,
                                    text=" Select Product Name",
                                    font= ("Arial",22))

product_name_select_label1.place(            relx=0.387,
                                            rely=0.35,
                                            relwidth=0.22,
                                            relheight=0.06)

back_to_product_management_button = CTkButton( delete_product_frame,
                                            command = open_product_management,
                                            text = "Back",
                                            width = 155,
                                            height = 30,
                                            font =("Arial", 17))

back_to_product_management_button.place(
                                            relx=0.8,
                                            rely=0.8,
                                            relwidth=0.08,
                                            relheight=0.06)

# view products page

view_product_title = CTkLabel(view_product_frame,text = " View Product Details" , font =("Arial", 30))
view_product_title.place(
                                relx=0.25,
                                rely=0.07,
                                relwidth=0.5,
                                relheight=0.1)



#basically i found 2 ways to do it, one is the treeview thing , or this complicated grid view, im just seeing which looks better now

# this is the grid way
product_table_frame = CTkScrollableFrame(view_product_frame, fg_color= "black")


product_table_frame.place(relx = 0.1,
                      rely = 0.35,
                      relwidth= 0.65,
                      relheight= 0.6)

# i have to create the headings for the table, like column names, so ill create labels

id_heading = CTkLabel(product_table_frame, text = "PID",  font= ("Helvectica" , 20, "bold"))
name_heading = CTkLabel(product_table_frame, text = "Product Name", font= ("Helvectica" , 20 , "bold"))
price_heading = CTkLabel(product_table_frame, text = "Price", font= ("Helvectica" , 20, "bold"))
cost_heading = CTkLabel(product_table_frame, text = "Cost", font= ("Helvectica" , 20 , "bold"))

#i want to maintain some space between the grids ,and stuff
id_heading.grid(row = 0, column = 0, padx = 38, pady = 15)
name_heading.grid(row = 0, column = 1, padx = 68, pady = 15)
price_heading.grid(row = 0, column = 2, padx = 38, pady = 15)
cost_heading.grid(row = 0 , column = 3, padx = 38, pady = 15)

#i will have to let the columns expand if the names are too big or smt.

product_table_frame.grid_columnconfigure(0, weight = 0)
product_table_frame.grid_columnconfigure(1, weight = 2)
product_table_frame.grid_columnconfigure(2, weight = 1)
product_table_frame.grid_columnconfigure(3, weight = 1)

# i have to insert all the rows and stuff,
# i think i have to make a whole different loops for every column here.

#i am creating these labels so I can destroy the unecessary labels when I go back to product management frame.
id_label = CTkLabel(product_table_frame)

name_label = CTkLabel(product_table_frame)

price_label = CTkLabel (product_table_frame)


cost_label = CTkLabel(product_table_frame)

#i will be creating a search bar. For that i have to put in entries and then the placeholder text etc.

search_bar  = CTkEntry(view_product_frame, placeholder_text= "Search Products")

search_bar.place(relx = 0.1,
                  rely = 0.24,
                 relwidth = 0.4,
                 relheight = 0.055)

search_text = search_bar.get()

products = system.get_all_products()




def columns_placing (search_text = ""):

    #i am destroying the widgets everytime to keep the frame clean

    for widget in product_table_frame.winfo_children():
        widget.destroy()

    # i have to create the labels again since the old labels are going away. ill make the heading come back by creating them again

    id_heading = CTkLabel(product_table_frame, text="PID", font=("Helvectica", 20, "bold"))
    name_heading = CTkLabel(product_table_frame, text="Product Name", font=("Helvectica", 20, "bold"))
    price_heading = CTkLabel(product_table_frame, text="Price", font=("Helvectica", 20, "bold"))
    cost_heading = CTkLabel(product_table_frame, text="Cost", font=("Helvectica", 20, "bold"))

    # i want to maintain some space between the grids ,and stuff
    id_heading.grid(row=0, column=0, padx=38, pady=15)
    name_heading.grid(row=0, column=1, padx=68, pady=15)
    price_heading.grid(row=0, column=2, padx=38, pady=15)
    cost_heading.grid(row=0, column=3, padx=38, pady=15)

    products = system.get_all_products()

    for row_index, product in enumerate(products, start = 1):

            #i will continuously label these labels.

            if search_text.lower() in product.name.lower() :
                id_label = CTkLabel(product_table_frame,
                                    text=str(product.product_ID), text_color="#D3D3D3")

                name_label = CTkLabel(product_table_frame,
                                      text=str(product.name), text_color="#D3D3D3")

                price_label = CTkLabel(product_table_frame,
                                       text=str(product.selling_price), text_color="#D3D3D3")

                cost_label = CTkLabel(product_table_frame,
                                      text=str(product.cost), text_color="#D3D3D3")

                id_label.grid(row=row_index, column=0)
                name_label.grid(row=row_index, column=1)
                price_label.grid(row=row_index, column=2)
                cost_label.grid(row=row_index, column=3)



def search_products(event):
    columns_placing(search_bar.get())



search_bar.bind("<KeyRelease>", search_products)


def double_function ():
    open_view_product_frame()
    columns_placing()



product_management_view_product_button.configure( command = double_function)


def destroy_labels ():
    for widget in product_table_frame.winfo_children():
        widget.destroy()





back_to_product_management_button_view_frame = CTkButton(view_product_frame,
                                              command= open_product_management,
                                              text = "Back",
                                              width = 155,
                                              height = 30,
                                              font = ("Arial", 17))

# i will create a double function and configue it to do the thing.


back_to_product_management_button_view_frame.place (
                                            relx=0.85,
                                            rely=0.891,
                                            relwidth=0.08,
                                            relheight=0.06)


# i will create a double function and configue it to do the thing.

def double_function_for_destory ():
    open_product_management()
    destroy_labels()
    search_bar.delete(0, "end")



back_to_product_management_button_view_frame.configure(command= double_function_for_destory)





#sales management

def open_sales_management():
    sales_management_frame.tkraise()



sales_management_button = CTkButton(
        home_frame,
        command= open_sales_management,
        text = "Sales Management",
        width = 250, height = 50,
        font =("Arial", 20, ))

sales_management_button.pack(pady=(0,10))

#inside sales management frame stuff
sales_management_title = CTkLabel(sales_management_frame,text = "Sales Management" , font =("Arial", 30))
sales_management_title.place(
                                relx=0.0001,
                                rely=0.1,
                                relwidth=0.5,
                                relheight=0.1)

sales_management_close_button = CTkButton(sales_management_frame,
                                          command= go_back_to_home_function,
                                          text = "Back",
                                          width = 150,
                                          height = 35,
                                          font =("Arial", 13))

sales_management_close_button.place(
                                            relx=0.85,
                                            rely=0.85,
                                            relwidth=0.07,
                                            relheight=0.07)

button_container_sales_management = CTkFrame(sales_management_frame,fg_color="transparent")
button_container_sales_management.place(
                        relx=0.15,
                        rely=0.3,
                        relwidth=0.2,
                        relheight=0.4)

#for every option within the product management section, I need another frame since its a new page in itself.
#so ill make frames for all of these buttons making it easier later on.

# back to sales management page

back_to_sales_management_button = CTkButton( add_sales_record_frame,
                                            command = open_sales_management,
                                            text = "Back",
                                            width = 155,
                                            height = 30,
                                            font =("Arial", 17))



def open_add_sales_record_frame():
    add_sales_record_frame.tkraise()


def open_view_sales_record_frame():
    view_sales_record_frame.tkraise()


def open_update_sales_record_frame():
    update_sales_record_frame.tkraise()


def open_delete_sales_record_frame():
    delete_sales_record_frame.tkraise()


sales_management_add_sales_record_button = CTkButton(button_container_sales_management,
                                                  command = open_add_sales_record_frame,
                                                  text = " Add Sales Record",
                                                  width = 200,
                                                  height = 45,
                                                  font = ("Arial", 20))

sales_management_view_sales_record_button = CTkButton(button_container_sales_management,
                                                          command = open_view_sales_record_frame,
                                                          text = "View Sales Records",
                                                          width=200,
                                                          height=45,
                                                          font=("Arial", 20))

sales_management_update_sales_record_button = CTkButton(button_container_sales_management,
                                                            command = open_update_sales_record_frame,
                                                            text = "Update Sales Records",
                                                            width = 200,
                                                            height = 45,
                                                            font = ("Arial", 19))

sales_management_delete_sales_record_button = CTkButton(button_container_sales_management,
                                             command = open_delete_sales_record_frame,
                                             text= " Delete Sales Records",
                                             width = 200,
                                             height = 45,
                                             font = ("Arial", 19))


sales_management_add_sales_record_button.pack(pady = (0,10))
sales_management_view_sales_record_button.pack(pady = (0,10))
sales_management_update_sales_record_button.pack(pady=(0,10))
sales_management_delete_sales_record_button.pack(pady = (0,10))

# ill write this code for the add sales record page now

add_sales_record_title = CTkLabel(add_sales_record_frame,text = "Add New Sales Record " , font =("Arial", 30))
add_sales_record_title.place(
                                relx=0.0001,
                                rely=0.1,
                                relwidth=0.5,
                                relheight=0.1)

# now i will write the function for the code of the adding the sales record

def adding_sales_record ():

    #i got the product name from the combobox
    product_name = product_name_select_combobox.get()

    #using the get thing, i got the name and now I can use it to get the product it.
    product_ID = system.get_product_ID_by_name(product_name)

    valid = True
    #all the validation cases:
    #empty product selection
    # empty quantity
    #negative quantity
    #alphabets in quantity

    success_label = CTkLabel(add_sales_record_frame,
                             text="",
                             text_color="green")

    #im creating a sub function to call it when the button is clicked so 3 seconds later the label disappears.
    def clear_success_label():
        success_label.configure(text = "")

    def clear_error_label ():
        error_label.configure(text = "")


    # error label i will use so i can configure it based on the type of error.
    error_label = CTkLabel(add_sales_record_frame,
                           text="",
                           text_color="red")

    error_label.place(relx=0.17,
                      rely = 0.66,
                      relwidth=0.15,
                      relheight=0.07
                      )


    #validation for the dropbox
    if product_name_select_combobox.get() == "":
        valid = False

        error_label.configure(text="Selection cannot be empty")
        error_label.place_configure(relx=0.149,
                                    rely=0.42,
                                    relwidth=0.2,
                                    relheight=0.07)
        error_label.after(3000, clear_error_label)

        product_name_select_combobox.focus()
        return

    products_names = system.get_all_product_names()
    if product_name_select_combobox.get() not in products_names:
        valid = False
        error_label.configure(text=" Please select product from the list only")
        error_label.place(relx=0.1289,
                                    rely=0.42,
                                    relwidth=0.25,
                                    relheight=0.07)
        error_label.after(3000, clear_error_label)
        product_name_select_combobox.focus()
        return


    #quantity validation
    quantity = sales_quantity_entry.get()

    if quantity.strip() == "":

        valid = False
        error_label.configure(text="Sales quantity cannot be empty")
        error_label.place_configure(relx=0.15,
                                    rely=0.66,
                                    relwidth=0.2,
                                    relheight=0.07)
        error_label.after(3000, clear_error_label)
        sales_quantity_entry.focus()
        return


    try:
        quantity = int(sales_quantity_entry.get())

        if quantity <= 0:
            #show the enter a positive value error message
            valid = False
            error_label.configure(text= "Sales quantity cannot be negative")
            error_label.place_configure( relx=0.15,
                                         rely = 0.66,
                                         relwidth=0.2,
                                         relheight=0.07)
            error_label.after(3000, clear_error_label)
            sales_quantity_entry.focus()
            return


    except ValueError:

        #show the error message if user entered alphabets instead of numeric values
        valid = False
        error_label.configure(text=" Cannot have alphabets or a decimal number")
        error_label.place_configure(relx=0.15,
                                    rely = 0.66,
                                    relwidth=0.27,
                                    relheight=0.07)

        error_label.after(3000, clear_error_label)

        sales_quantity_entry.focus()
        return

    if valid:
        system.add_sales(product_ID,quantity)
        success_label.configure(
                             text="Sales record added successfully!")

        success_label.place(relx=0.33,
                            rely=0.77,
                            relwidth=0.2,
                            relheight=0.06)
        sales_quantity_entry.delete(0, "end")
        success_label.after(3000,clear_success_label)
        product_name_select_combobox.set("")



add_sales_record_button = CTkButton(add_sales_record_frame,
                               command= adding_sales_record,
                               text = "Add Sales Record" ,
                               width = 175,
                               height = 22,
                               font=("Arial",17 ))

add_sales_record_button.place(
                                            relx=0.17,
                                            rely=0.77,
                                            relwidth=0.15,
                                            relheight=0.06)


# im creating like a selection box thing, so for that I need the list of products for getting all the product names
# ill create this function to get all the names separately in the core system so it will be updating it all the time


list_products = system.get_all_product_names()

product_name_select_combobox = CTkComboBox(add_sales_record_frame, values = list_products,width=190,
                                            height = 41)
product_name_select_combobox.set("")


product_name_select_combobox.place(         relx=0.16,
                                            rely=0.36,
                                            )


product_name_select_label = CTkLabel(add_sales_record_frame,
                                    text=" Select Product Name",
                                    font= ("Arial",22))

product_name_select_label.place(            relx=0.145,
                                            rely=0.28,
                                            relwidth=0.22,
                                            relheight=0.06)


sales_quantity_entry = CTkEntry(add_sales_record_frame)

sales_quantity_entry.place(                  relx=0.17,
                                            rely=0.6,
                                            relwidth=0.152,
                                            relheight=0.06)

sales_quantity_entry_label = CTkLabel(add_sales_record_frame,
                                    text="Enter Quantity",
                                    font=("Arial", 22))

sales_quantity_entry_label.place(           relx=0.16,
                                            rely=0.53,
                                            relwidth=0.17,
                                            relheight=0.06)

back_to_sales_management_button.place(
                                            relx=0.8,
                                            rely=0.8163,
                                            relwidth=0.08,
                                            relheight=0.06)


#view sales page.

view_sales_title = CTkLabel(view_sales_record_frame,text = " View Sales Details" , font =("Arial", 30))
view_sales_title.place(
                                relx=0.25,
                                rely=0.07,
                                relwidth=0.5,
                                relheight=0.1)



#basically i found 2 ways to do it, one is the treeview thing , or this complicated grid view, im just seeing which looks better now

# this is the grid way
sales_records_table_frame = CTkScrollableFrame(view_sales_record_frame, fg_color= "black")


sales_records_table_frame.place(relx = 0.1,
                      rely = 0.35,
                      relwidth= 0.65,
                      relheight= 0.6)



#i will have to let the columns expand if the names are too big or smt.

sales_records_table_frame.grid_columnconfigure(0, weight = 0)
sales_records_table_frame.grid_columnconfigure(1, weight = 1)
sales_records_table_frame.grid_columnconfigure(2, weight = 2)
sales_records_table_frame.grid_columnconfigure(3, weight = 1)
sales_records_table_frame.grid_columnconfigure(4, weight = 1)


# i have to insert all the rows and stuff,
# i think i have to make a whole different loops for every column here.

#i am creating these labels so I can destroy the unecessary labels when I go back to product management frame.
RID_label = CTkLabel(sales_records_table_frame)

PID_label = CTkLabel(sales_records_table_frame)

product_name_view_sales_heading_label = CTkLabel(sales_records_table_frame)

date_label = CTkLabel(sales_records_table_frame)


quantity_label = CTkLabel(sales_records_table_frame)

#i will be creating a search bar. For that i have to put in entries and then the placeholder text etc.

search_bar_view_sales  = CTkEntry(view_sales_record_frame, placeholder_text= "Search sales")

search_bar_view_sales.place(relx = 0.1,
                  rely = 0.24,
                 relwidth = 0.4,
                 relheight = 0.055)

search_text_view_sales = search_bar_view_sales.get()



def columns_placing_view_sales (search_text_view_sales = ""):

    #i am destroying the widgets everytime to keep the frame clean

    for widget in sales_records_table_frame.winfo_children():
        widget.destroy()

    RID_heading = CTkLabel(sales_records_table_frame, text="RID", font=("Helvectica", 20, "bold"))
    PID_heading = CTkLabel(sales_records_table_frame, text="PID", font=("Helvectica", 20, "bold"))
    product_name_view_sales_heading = CTkLabel(sales_records_table_frame, text="Product Name",
                                               font=("Helvectica", 20, "bold"))
    date_heading = CTkLabel(sales_records_table_frame, text="Date", font=("Helvectica", 20, "bold"))
    quantity_heading = CTkLabel(sales_records_table_frame, text="Quantity", font=("Helvectica", 20, "bold"))

    # i want to maintain some space between the grids ,and stuff
    RID_heading.grid(row=0, column=0, padx=30, pady=15)
    PID_heading.grid(row=0, column=1, padx=30, pady=15)
    product_name_view_sales_heading.grid(row=0, column=2, padx=40, pady=15)
    date_heading.grid(row=0, column=3, padx=30, pady=15)
    quantity_heading.grid(row=0, column=4, padx=20, pady=15)



    sales_records = system.get_all_sales_records()


    for row_index, sale in enumerate(sales_records, start = 1):

        product_name = system.get_product_name_by_ID(sale.product_ID).lower()

        if search_text_view_sales.lower() in product_name:
            #i will continuously create labels and place them. For that, Im using ts loop .

                RID_label = CTkLabel(sales_records_table_frame,
                                    text=str(sale.record_ID), text_color="#D3D3D3")

                PID_label = CTkLabel(sales_records_table_frame,
                                     text=str(sale.product_ID), text_color="#D3D3D3")

                name_label = CTkLabel(sales_records_table_frame,
                                      text=str(system.get_product_name_by_ID(sale.product_ID)), text_color="#D3D3D3")

                date_label = CTkLabel(sales_records_table_frame,
                                       text=str(sale.date) , text_color="#D3D3D3")

                quantity_label = CTkLabel(sales_records_table_frame,
                                      text=str(sale.quantity), text_color="#D3D3D3")

                RID_label.grid(row=row_index, column=0)
                PID_label.grid(row=row_index, column=1)
                name_label.grid(row=row_index, column=2)
                date_label.grid(row=row_index, column=3)
                quantity_label.grid(row=row_index, column=4)



def search_sales_records(event):
    columns_placing_view_sales(search_bar_view_sales.get())



search_bar_view_sales.bind("<KeyRelease>", search_sales_records)


def double_function_view_sales ():
    open_view_sales_record_frame()
    columns_placing_view_sales()



sales_management_view_sales_record_button.configure( command = double_function_view_sales)


def destroy_labels_view_sales ():
    for widget in sales_records_table_frame.winfo_children():
        widget.destroy()





back_to_sales_management_button_view_frame = CTkButton(view_sales_record_frame,
                                              command= open_sales_management,
                                              text = "Back",
                                              width = 155,
                                              height = 30,
                                              font = ("Arial", 17))

# i will create a double function and configue it to do the thing.


back_to_sales_management_button_view_frame.place (
                                            relx=0.85,
                                            rely=0.891,
                                            relwidth=0.08,
                                            relheight=0.06)


# i will create a double function and configue it to do the thing.
def double_function_for_destroy_view_sales ():
    open_sales_management()
    destroy_labels_view_sales()
    search_bar_view_sales.delete(0, "end")



back_to_sales_management_button_view_frame.configure(command= double_function_for_destroy_view_sales)


#update sales record page.
update_sales_title = CTkLabel(update_sales_record_frame,text = "Update Sales Details" , font =("Arial", 30))
update_sales_title.place(
                                relx=0.0001,
                                rely=0.1,
                                relwidth=0.5,
                                relheight=0.1)

back_to_sales_management_update_sales_button = CTkButton(update_sales_record_frame,
                                              text = "Back",
                                              width = 155,
                                              height = 27,
                                              font = ("Arial", 17))

back_to_sales_management_update_sales_button.place(
                                            relx=0.8,
                                            rely=0.855,
                                            relwidth=0.08,
                                            relheight=0.06)

list_products2 = system.get_all_product_names()

product_name_select_4_combobox = CTkComboBox(update_sales_record_frame, values = list_products2,width=200,
                                            height = 41,)

product_name_select_4_combobox.set("")

product_name_select_4_combobox.place(       relx=0.16,
                                            rely=0.3)

product_name_select_4_label = CTkLabel(update_sales_record_frame,
                                    text=" Select Product",
                                    font= ("Arial",22))

product_name_select_4_label.place(          relx=0.13,
                                            rely=0.23,
                                            relwidth=0.25,
                                            relheight=0.06)

# basically I need to display the current condition of the products , because this is more helpful for the user
# what i can do is create new widgets and display upon the name selection. When the name is selected, I can display it accordingly
# i cant use place forget when a product detial is update, so I have create the labels outside the function


#i am creating the main bigger labels here.
current_product_label1 = CTkLabel(update_sales_record_frame,
                              text="Current Product: ",
                              font=("Arial", 20),
                              )
current_date_label = CTkLabel(update_sales_record_frame,
                              text="Current Date: ",
                              font=("Arial", 20),
                              )

current_quantity_label = CTkLabel(update_sales_record_frame,
                               text="Current Quantity: ",
                               font=("Arial", 20))




# i am making sub labels so ill place them next to the labels with a colon so it will look better .

current_product_sub_label1 = CTkLabel(update_sales_record_frame,
                                  font=("Arial", 17))

current_date_sub_label = CTkLabel(update_sales_record_frame,
                                  font=("Arial", 17))
current_quantity_sub_label = CTkLabel(update_sales_record_frame,
                                   font=("Arial", 17))

# label and combobox for selecting RID.

select_RID_label = CTkLabel(update_sales_record_frame, text=" Select RID ",
                               font=("Arial", 22))

select_RID_label.place(relx=0.155,
                         rely=0.4315,
                         relwidth=0.2,
                         relheight=0.06)

select_RID_combobox = CTkComboBox(update_sales_record_frame, width=  200, height = 41)

select_RID_combobox.place(relx=0.16,
                         rely=0.5013)

select_RID_combobox.set("")



# basically i have to create a double function, based on what the user selects, I have to update the RID list accordingly.
# for that ill create a function for the


def display_current_values_update_sales_and_RID_list (sonion):


    #i am setting values here because i set combobox to empty over there and its creating a stupid bug
    current_product = product_name_select_4_combobox.get()
    product_ID = system.get_product_ID_by_name(product_name_select_4_combobox.get())
    current_quantity = None
    current_date = None

    sales_records = system.get_all_sales_records()

    # create the for loop for the updating respective RID.
    list_of_RID = []

    for i in sales_records:
        if i.product_ID == product_ID:

            list_of_RID.append(i.record_ID)

    select_RID_combobox.configure(values=list_of_RID)

    for i in sales_records:
        if i.record_ID == select_RID_combobox.get():
            current_quantity = i.quantity
            current_date = i.date

    #i will configure these values when the function is called so real-time values are there.
    current_product_sub_label1.configure(text = str(current_product))
    current_date_sub_label.configure(text = current_date)
    current_quantity_sub_label.configure(text= str(current_quantity))



    update_sales_record_frame.update_idletasks()


    current_product_label1.place(           relx=0.415,
                                            rely=0.24,
                                            relwidth=0.25,
                                            relheight=0.06)

    current_product_sub_label1.place(       relx=0.62,
                                            rely=0.24,
                                            relwidth=0.25,
                                            relheight=0.06)


    current_date_label.place(               relx=0.4,
                                            rely=0.33,
                                            relwidth=0.25,
                                            relheight=0.06)

    current_date_sub_label.place(           relx=0.64,
                                            rely=0.33,
                                            relwidth = 0.2,
                                            relheight = 0.06)

    current_quantity_label.place(              relx=0.415,
                                            rely=0.43,
                                            relwidth=0.25,
                                            relheight=0.06)

    current_quantity_sub_label.place(          relx=0.62,
                                            rely=0.43,
                                            relwidth = 0.2,
                                            relheight = 0.06)


product_name_select_4_combobox.configure(command = display_current_values_update_sales_and_RID_list)
select_RID_combobox.configure(command = display_current_values_update_sales_and_RID_list)


# i am creating labels and entries that will adapt to the type of change so i can the GUI more clean
temp_entry1 = CTkEntry(update_sales_record_frame)
temp_label1 = CTkLabel(update_sales_record_frame)


#so basically, i need two drop downs, one for the products, the other for the product's RID. Then they will select the new product
#if the change was product, or they will take the quantity and change that.

# one is for selecting new product the other is for selecting the respective RID
temp_combobox1 = CTkComboBox(update_sales_record_frame, values = list_products2 , width = 200, height = 41)

temp_combobox1.set("")


list_of_change2 = ["Product", "Quantity"]
select_change_combobox2 = CTkComboBox( update_sales_record_frame,
                                     values=list_of_change2,
                                     width=200,
                                     height=41)

select_change_combobox2.place(relx=0.16,
                             rely=0.7)

select_change_combobox2.set("")

select_change_label2 = CTkLabel(update_sales_record_frame,
                               text=" Select change type",
                               font=("Arial", 22))


select_change_label2.place(                  relx=0.145,
                                            rely=0.63,
                                            relwidth=0.22,
                                            relheight=0.06)

#update button itself.
update_sales_record_button = CTkButton(update_sales_record_frame,
                               text = "Update Details" ,
                               width = 175,
                               height = 22,
                               font=("Arial",17 ) )



#i need the 3 seconds disappear thing

def selection_widget_showup_update_sales(son):

    temp_label.place(relx=0.14,
                     rely=0.625,
                     relwidth=0.25,
                     relheight=0.06)

    update_sales_record_button.place(
        relx=0.5,
        rely=0.8,
        relwidth=0.13,
        relheight=0.06)

    if select_change_combobox2.get() == "Product":

        temp_entry1.place_forget()
        temp_label1.configure(text=" Select new product ",
                             font=("Arial", 22))

        temp_label1.place(relx=0.465,
                         rely=0.5415,
                         relwidth=0.2,
                         relheight=0.06)


        temp_combobox1.place(relx=0.463,
                         rely=0.61)


    if select_change_combobox2.get() == "Quantity" :

        temp_combobox1.place_forget()
        temp_label1.configure(text=" Enter new quantity",
                             font=("Arial", 22))
        temp_label1.place_configure(relx=0.46,
                         rely=0.5415,
                         relwidth=0.2,
                         relheight=0.06)

        temp_entry1.configure(width = 200, height = 41)
        temp_entry1.place(relx=0.463,
                         rely=0.61)




select_change_combobox2.configure(command = selection_widget_showup_update_sales)



def update_sales_record_details_GUI ():

    name = product_name_select_4_combobox.get()

    success_label= CTkLabel(update_sales_record_frame,
                              text="",
                              text_color="green")

    success_label.place(relx=0.43,
                              rely=0.86,
                              relwidth=0.27,
                              relheight=0.07)

    error_label = CTkLabel(update_sales_record_frame,
                           text="",
                           text_color="red")

    error_label.place(relx=0.16,
                              rely=0.565,
                              relwidth=0.2,
                              relheight=0.07)

    def clear_success_label ():
        success_label.configure(text = "")

    def clear_error_label ():
        error_label.configure(text = "")


    if product_name_select_4_combobox.get().strip() == "" :
        valid = False

        error_label.configure(text="Selection cannot be empty")
        error_label.place(          relx=0.16,
                                    rely=0.37,
                                    relwidth=0.2,
                                    relheight=0.06)
        error_label.after(3000, clear_error_label)

        product_name_select_2_combobox.focus()
        return

    products_names = system.get_all_product_names()
    if product_name_select_4_combobox.get() not in products_names:

            valid = False
            error_label.configure(text=" Please select product from the list only")
            error_label.place(relx=0.137,
                              rely=0.37,
                              relwidth=0.25,
                              relheight=0.06)
            error_label.after(3000, clear_error_label)
            product_name_select_4_combobox.focus()
            return


    #i have to validate the RID combobox.
    #2 validations, one is the empty combobox, the other one is the , nonexist RID thing.

    if select_RID_combobox.get() == "":
        valid = False
        error_label.configure(text="RID selection cannot be empty")
        error_label.place(relx=0.134,
                          rely=0.56,
                          relwidth=0.25,
                          relheight=0.06)
        error_label.after(3000, clear_error_label)
        select_RID_combobox.focus()
        return

    # i am doing the not in the rid list validation nonense.

    sales_records = system.get_all_sales_records()
    list_of_RID = []

    RID_checking_product_ID = system.get_product_ID_by_name(product_name_select_4_combobox.get())

    for i in sales_records:
        if i.product_ID == RID_checking_product_ID:
            list_of_RID.append(i.record_ID)


    if select_RID_combobox.get() not in list_of_RID:
        valid = False
        error_label.configure(text="Choose RID only from the list")
        error_label.place(relx=0.134,
                          rely=0.56,
                          relwidth=0.25,
                          relheight=0.06)
        error_label.after(3000, clear_error_label)
        select_RID_combobox.focus()
        return



    if select_change_combobox2.get().strip() == "":

        valid = False
        error_label.configure(text="Selection cannot be empty")
        error_label.place(relx=0.16,
                          rely=0.76,
                          relwidth=0.2,
                          relheight=0.06)
        error_label.after(3000, clear_error_label)
        return


     # i basically found this bug, where I can type into the combobox and bypass everything. So i need to validate it
    if select_change_combobox2.get() not in list_of_change2:
        valid = False

        error_label.configure(text="Select the changes given in the list")
        error_label.place(relx=0.1372,
                          rely=0.76,
                          relwidth=0.25,
                          relheight=0.06)
        error_label.after(3000, clear_error_label)
        return


    # this entire thing is for the product.
    if select_change_combobox2.get() == "Product":

        valid = True # since the change selected is correct.

        new_name = temp_combobox1.get()

        product_ID = system.get_product_ID_by_name(name)
        valid = True

        if new_name == "":

            valid = False

            error_label.configure(text="Name cannot be empty")
            error_label.place(relx=0.4265,
                              rely=0.67,
                              relwidth=0.27,
                              relheight=0.07)
            error_label.after(3000, clear_error_label)
            temp_combobox1.focus()
            return

        # i need to basically not let the user enter the same product name and a nonexistent product name.

        if new_name == product_name_select_4_combobox.get() :
            valid = False
            error_label.configure(text="Name cannot be the same as previous one")
            error_label.place(relx=0.4265,
                              rely=0.67,
                              relwidth=0.27,
                              relheight=0.07)
            error_label.after(3000, clear_error_label)
            temp_combobox1.focus()
            return

        if new_name not in products_names:
            valid = False
            error_label.configure(text="Select product from the list only")
            error_label.place(relx=0.43,
                              rely=0.67,
                              relwidth=0.27,
                              relheight=0.07)
            error_label.after(3000, clear_error_label)
            temp_combobox1.focus()
            return


        if valid:
            new_name = temp_combobox1.get()
            new_product_ID = system.get_product_ID_by_name(new_name)
            record_ID = select_RID_combobox.get()
            system.database.update_sales_record_product(record_ID,new_product_ID)
            success_label.configure(text="Detail Updated Successfully!")
            success_label.after(3000, clear_success_label)
            product_name_select_4_combobox.set("")
            select_change_combobox2.set("")
            select_RID_combobox.set("")
            temp_label1.place_forget()
            temp_combobox1.set("")
            temp_combobox1.place_forget()
            current_product_label1.place_forget()
            current_product_sub_label1.place_forget()
            current_date_label.place_forget()
            current_date_sub_label.place_forget()
            current_quantity_label.place_forget()
            current_quantity_sub_label.place_forget()
            update_sales_record_button.place_forget()


    #this only for quantity change
    if select_change_combobox2.get() == "Quantity" :

        name = product_name_select_4_combobox.get()
        product_ID = system.get_product_ID_by_name(name)
        new_quantity = temp_entry1.get()
        valid = True

        if  new_quantity == "":
            valid = False

            error_label.configure(text="Quantity cannot be empty")
            error_label.place(relx=0.43,
                              rely=0.67,
                              relwidth=0.27,
                              relheight=0.07)
            error_label.after(3000, clear_error_label)

            temp_entry1.focus()
            return

        try:
            new_quantity = int(temp_entry1.get())
            if  new_quantity <= 0 :
                valid = False

                error_label.configure(text="Quantity cannot be negative or zero")
                error_label.place(relx=0.43,
                              rely=0.67,
                              relwidth=0.27,
                              relheight=0.07)
                error_label.after(3000, clear_error_label)

                temp_entry1.focus()
                return

        except ValueError:

            valid = False

            error_label.configure(text="Quantity cannot have alphabets")
            error_label.place(relx=0.43,
                              rely=0.67,
                              relwidth=0.27,
                              relheight=0.07)
            error_label.after(3000, clear_error_label)

            temp_entry1.focus()
            return

        if valid:

            record_ID = select_RID_combobox.get()
            system.database.update_sales_record_quantity(record_ID,new_quantity)
            success_label.configure(text="Detail Updated Successfully!")
            success_label.after(3000, clear_success_label)
            product_name_select_4_combobox.set("")
            select_change_combobox2.set("")
            select_RID_combobox.set("")
            temp_label1.place_forget()
            temp_entry1.delete(0, "end")
            temp_entry1.place_forget()
            current_product_label1.place_forget()
            current_product_sub_label1.place_forget()
            current_date_label.place_forget()
            current_date_sub_label.place_forget()
            current_quantity_label.place_forget()
            current_quantity_sub_label.place_forget()
            update_sales_record_button.place_forget()



update_sales_record_button.configure(command= update_sales_record_details_GUI)

def double_function_update_sales_record ():
    open_sales_management()
    product_name_select_4_combobox.set("")
    select_change_combobox2.set("")
    select_RID_combobox.set("")
    temp_label1.place_forget()
    temp_entry1.delete(0, "end")
    temp_entry1.place_forget()
    current_product_label1.place_forget()
    current_product_sub_label1.place_forget()
    current_date_label.place_forget()
    current_date_sub_label.place_forget()
    current_quantity_label.place_forget()
    current_quantity_sub_label.place_forget()
    update_sales_record_button.place_forget()

back_to_sales_management_update_sales_button.configure(command = double_function_update_sales_record)

#delete sales record page

delete_sales_record_title = CTkLabel(delete_sales_record_frame,text = "Delete sales records" , font =("Arial", 30))
delete_sales_record_title.place(
                                relx=0.0001,
                                rely=0.1,
                                relwidth=0.5,
                                relheight=0.1)

back_to_sales_management_delete_sales_button = CTkButton(delete_sales_record_frame,
                                              command= open_sales_management,
                                              text = "Back",
                                              width = 155,
                                              height = 27,
                                              font = ("Arial", 17))

back_to_sales_management_delete_sales_button.place(
                                            relx=0.8,
                                            rely=0.855,
                                            relwidth=0.08,
                                            relheight=0.06)

#user gets to select product, then the respective RID then gets to delete it. Show the current details and then let them delete it



list_products3 = system.get_all_product_names()

product_name_select_5_combobox = CTkComboBox(delete_sales_record_frame, values = list_products3, width=200,
                                            height = 41,)

product_name_select_5_combobox.set("")

product_name_select_5_combobox.place(       relx=0.16,
                                            rely=0.3)

product_name_select_5_label = CTkLabel(delete_sales_record_frame,
                                    text=" Select Product",
                                    font= ("Arial",22))

product_name_select_5_label.place(          relx=0.13,
                                            rely=0.23,
                                            relwidth=0.25,
                                            relheight=0.06)

current_product_label2 = CTkLabel(delete_sales_record_frame,
                              text="Current Product: ",
                              font=("Arial", 20),
                              )
current_date_label2 = CTkLabel(delete_sales_record_frame,
                              text="Current Date: ",
                              font=("Arial", 20),
                              )

current_quantity_label2= CTkLabel(delete_sales_record_frame,
                               text="Current Quantity: ",
                               font=("Arial", 20))




# i am making sub labels so ill place them next to the labels with a colon so it will look better .

current_product_sub_label2 = CTkLabel(delete_sales_record_frame,
                                  font=("Arial", 17))

current_date_sub_label2 = CTkLabel(delete_sales_record_frame,
                                  font=("Arial", 17))
current_quantity_sub_label2 = CTkLabel(delete_sales_record_frame,
                                   font=("Arial", 17))

# label and combobox for selecting RID.

select_RID_label1 = CTkLabel(delete_sales_record_frame, text=" Select RID ",
                               font=("Arial", 22))

select_RID_label1.place(relx=0.155,
                         rely=0.4315,
                         relwidth=0.2,
                         relheight=0.06)

select_RID_combobox2 = CTkComboBox(delete_sales_record_frame, width=  200, height = 41)

select_RID_combobox2.place(relx=0.16,
                         rely=0.5013)

select_RID_combobox2.set("")



# basically i have to create a double function, based on what the user selects, I have to update the RID list accordingly.
# for that ill create a function for the

#the delete button
delete_sales_record_button = CTkButton(delete_sales_record_frame,
                               text = "Delete record" ,
                               width = 175,
                               height = 22,
                               font=("Arial",17 ) )

delete_sales_record_button.place(
                relx=0.195,
                rely=0.67,
                relwidth=0.13,
                relheight=0.06)


def display_current_values_delete_sales_and_RID_list (son):


    #i am setting values here because i set combobox to empty over there and its creating a stupid bug
    current_product = product_name_select_5_combobox.get()
    product_ID = system.get_product_ID_by_name(product_name_select_5_combobox.get())
    current_quantity = None
    current_date = None

    sales_records = system.get_all_sales_records()

    # create the for loop for the updating respective RID.
    list_of_RID = []

    for i in sales_records:
        if i.product_ID == product_ID:

            list_of_RID.append(i.record_ID)

    select_RID_combobox2.configure(values=list_of_RID)

    for i in sales_records:
        if i.record_ID == select_RID_combobox2.get():
            current_quantity = i.quantity
            current_date = i.date

    #i will configure these values when the function is called so real-time values are there.
    current_product_sub_label2.configure(text = str(current_product))
    current_date_sub_label2.configure(text = current_date)
    current_quantity_sub_label2.configure(text= str(current_quantity))



    update_sales_record_frame.update_idletasks()


    current_product_label2.place(           relx=0.415,
                                            rely=0.24,
                                            relwidth=0.25,
                                            relheight=0.06)

    current_product_sub_label2.place(       relx=0.62,
                                            rely=0.24,
                                            relwidth=0.25,
                                            relheight=0.06)


    current_date_label2.place(               relx=0.4,
                                            rely=0.33,
                                            relwidth=0.25,
                                            relheight=0.06)

    current_date_sub_label2.place(           relx=0.64,
                                            rely=0.33,
                                            relwidth = 0.2,
                                            relheight = 0.06)

    current_quantity_label2.place(              relx=0.415,
                                            rely=0.43,
                                            relwidth=0.25,
                                            relheight=0.06)

    current_quantity_sub_label2.place(          relx=0.62,
                                            rely=0.43,
                                            relwidth = 0.2,
                                            relheight = 0.06)


product_name_select_5_combobox.configure(command = display_current_values_delete_sales_and_RID_list)
select_RID_combobox2.configure(command = display_current_values_delete_sales_and_RID_list)

def delete_sales_record_details_GUI ():

    valid = True

    success_label= CTkLabel(delete_sales_record_frame,
                              text="",
                              text_color="green")

    success_label.place(relx=0.135,
                        rely=0.73,
                        relwidth=0.25,
                        relheight=0.06)

    error_label = CTkLabel(delete_sales_record_frame,
                           text="",
                           text_color="red")

    error_label.place(relx=0.16,
                              rely=0.565,
                              relwidth=0.2,
                              relheight=0.07)

    def clear_success_label ():
        success_label.configure(text = "")

    def clear_error_label ():
        error_label.configure(text = "")

    #all the validations for deletion.
    # product name empty and product name non existent . so 2 for name combobox
    # RID empty or RID non existent . so 2 for RID combobox
    #total 4 validations.

    #validation for name combobox empty
    if product_name_select_5_combobox.get().strip() == "" :
        valid = False

        error_label.configure(text="Selection cannot be empty")
        error_label.place(          relx=0.16,
                                    rely=0.37,
                                    relwidth=0.2,
                                    relheight=0.06)
        error_label.after(3000, clear_error_label)

        product_name_select_5_combobox.focus()
        return

    #validation for name combobox non existent name
    products_names = system.get_all_product_names()
    if product_name_select_5_combobox.get() not in products_names:

            valid = False
            error_label.configure(text=" Please select product from the list only")
            error_label.place(relx=0.137,
                              rely=0.37,
                              relwidth=0.25,
                              relheight=0.06)
            error_label.after(3000, clear_error_label)
            product_name_select_5_combobox.focus()
            return

    #validation for the RID combobox empty thing

    if select_RID_combobox2.get().strip() == "":
        valid = False
        error_label.configure(text="RID selection cannot be empty")
        error_label.place(relx=0.134,
                          rely=0.56,
                          relwidth=0.25,
                          relheight=0.06)
        error_label.after(3000, clear_error_label)
        select_RID_combobox2.focus()
        return


    #validation for non existent RID
    sales_records = system.get_all_sales_records()
    list_of_RID = []

    RID_checking_product_ID = system.get_product_ID_by_name(product_name_select_5_combobox.get())

    for i in sales_records:
        if i.product_ID == RID_checking_product_ID:
            list_of_RID.append(i.record_ID)


    if select_RID_combobox2.get() not in list_of_RID:
        valid = False
        error_label.configure(text="Choose RID only from the list")
        error_label.place(relx=0.134,
                          rely=0.56,
                          relwidth=0.25,
                          relheight=0.06)
        error_label.after(3000, clear_error_label)
        select_RID_combobox2.focus()
        return


    if valid:
        record_ID = select_RID_combobox2.get()
        system.database.delete_sales_record(record_ID)
        success_label.configure(text="Deleted successfully!")
        success_label.after(3000, clear_success_label)
        product_name_select_5_combobox.set("")
        select_RID_combobox2.set("")
        current_product_label2.place_forget()
        current_product_sub_label2.place_forget()
        current_date_label2.place_forget()
        current_date_sub_label2.place_forget()
        current_quantity_label2.place_forget()
        current_quantity_sub_label2.place_forget()

delete_sales_record_button.configure(command = delete_sales_record_details_GUI)

def destroy_widgets_delete_sales ():
    open_sales_management()
    product_name_select_5_combobox.set("")
    select_RID_combobox2.set("")
    current_product_label2.place_forget()
    current_product_sub_label2.place_forget()
    current_date_label2.place_forget()
    current_date_sub_label2.place_forget()
    current_quantity_label2.place_forget()
    current_quantity_sub_label2.place_forget()

back_to_sales_management_delete_sales_button.configure(command = destroy_widgets_delete_sales)





#analytics

def open_analytics_management():
    analytics_frame.tkraise()


analytics_button = CTkButton(home_frame,command= open_analytics_management, text = "Analytics", width = 250, height = 50, font =("Arial", 20, ))
analytics_button.pack(pady=(0,10))

# inside the analytics frame


analytics_title = CTkLabel(analytics_frame,text = "Analytics" , font =("Arial", 30))
analytics_title.place(
                                relx=0.0001,
                                rely=0.1,
                                relwidth=0.5,
                                relheight=0.1)

analytics_close_button = CTkButton(analytics_frame,
                                   command= go_back_to_home_function,
                                   text = "Back",
                                   width = 150,
                                   height = 35,
                                   font =("Arial", 13))
analytics_close_button.place(
                                            relx=0.85,
                                            rely=0.85,
                                            relwidth=0.07,
                                            relheight=0.07)

# this is the button container for analytics frame
button_container_analytics = CTkFrame(analytics_frame,fg_color="transparent")
button_container_analytics.place(
                        relx=0.15,
                        rely=0.3,
                        relwidth=0.17,
                        relheight=0.4)


def open_overview_analytics_frame():
    overview_frame_analytics_frame.tkraise()


def open_product_performance_frame():
    product_performance_analytics_frame.tkraise()


overview_button_analytics = CTkButton(button_container_analytics,
                                                  command = open_overview_analytics_frame,
                                                  text = "Overview",
                                                  width = 230,
                                                  height = 45,
                                                  font = ("Arial", 18))

product_performance_button_analytics = CTkButton(button_container_analytics,
                                                          command = open_product_performance_frame,
                                                          text = "Product Performance",
                                                          width=230,
                                                          height=45,
                                                          font=("Arial", 16.5))



overview_button_analytics.pack(pady = (10,15))
product_performance_button_analytics.pack(pady = (10,15))


#analytics overview frame

overview_analytics_title = CTkLabel(overview_frame_analytics_frame,text = "Overview" , font =("Arial", 30))
overview_analytics_title.place(
                                relx=0.0000001,
                                rely=0.05,
                                relwidth=0.5,
                                relheight=0.1)

back_to_analytics_overview_button = CTkButton(overview_frame_analytics_frame,
                                              command = open_analytics_management,
                                              text = "Back",
                                              width = 155,
                                              height = 27,
                                              font = ("Arial", 17))

back_to_analytics_overview_button.place(
                                            relx=0.85,
                                            rely=0.89,
                                            relwidth=0.08,
                                            relheight=0.06)

#i need to build summary cards for the overview of the products.

total_products_card = CTkFrame(overview_frame_analytics_frame)
total_products_card.place(relx=0.19,
                          rely=0.17,
                          relwidth=0.23,
                          relheight=0.18)

total_products_heading = CTkLabel(
    total_products_card,
    text="TOTAL PRODUCTS",
    font=("Arial", 16))

total_products_heading.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.25)

total_products_value = CTkLabel(
    total_products_card,
    text= str((system.get_no_of_products())),
    font=("Arial", 30, "bold"))

total_products_value.place(relx=0.1, rely=0.48, relwidth=0.8, relheight=0.4)


total_profit_card = CTkFrame(overview_frame_analytics_frame)
total_profit_card.place(relx=0.19,
                          rely=0.4,
                        relwidth=0.23,
                        relheight=0.18
                        )

total_profit_heading = CTkLabel(
    total_profit_card,
    text="TOTAL PROFIT",
    font=("Arial", 16))


total_profit_heading.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.25)

#i need to create backend fucntion for the total profit for all products thing.
total_profit_value = CTkLabel(
    total_profit_card,
    text= str((system.get_total_profit())),
    text_color= "green",
    font=("Arial", 30, "bold")
)


total_profit_value.place(relx=0.1, rely=0.48, relwidth=0.8, relheight=0.4)

#total units card
total_units_sold_card = CTkFrame(overview_frame_analytics_frame)
total_units_sold_card.place(relx=0.45,
                          rely=0.17,
                            relwidth=0.23,
                            relheight=0.18
                            )

#total units heading
total_units_sold_card_heading = CTkLabel(
    total_units_sold_card,
    text="TOTAL UNITS SOLD",
    font=("Arial", 16))


total_units_sold_card_heading.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.25)

#total units value label
total_units_sold_value = CTkLabel(
    total_units_sold_card,
    text= str((system.get_total_units_sold())),
    font=("Arial", 30, "bold"),
    text_color= "green")

total_units_sold_value.place(relx=0.1, rely=0.48, relwidth=0.8, relheight=0.4)

#best product card
best_product_card = CTkFrame(overview_frame_analytics_frame)
best_product_card.place(relx=0.45,
                          rely=0.4,
                        relwidth=0.23,
                        relheight=0.18
                        )

#best product card heading
best_product_card_heading = CTkLabel(
    best_product_card,
    text="BEST PRODUCT",
    font=("Arial", 16))



best_product_card_heading.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.25)

best_product_value = CTkLabel(
    best_product_card,
    text="24",
    font=("Arial", 30, "bold")
)
best_product_value.place(relx=0.1, rely=0.48, relwidth=0.8, relheight=0.4)

#i am creating a mini performance summary
#it will have start products, cash cows, etc stuff.

performance_summary_label = CTkLabel(overview_frame_analytics_frame,
                                     text = "Performance summary",
                                     font=("Arial", 20, "bold"))


performance_summary_label.place(relx=0.185,
                          rely=0.58,
                          relwidth=0.23,
                          relheight=0.12)


#i need to create labels and then sublabels for the performance summary since its updated upon user's asking.

#these are the main labels.

star_products_label_overview = CTkLabel(overview_frame_analytics_frame,
                                        text = "⭐ Star Products: ",
                                        font=("Helvetica",18))

star_products_label_overview.place(relx=0.1725,
                                    rely=0.68,
                                    relwidth=0.23,
                                    relheight=0.05)

cash_cows_product_label_overview = CTkLabel(overview_frame_analytics_frame,
                                            text = "💰🐄 Cash Cows :",
                                            font=("Helvetica",18))

cash_cows_product_label_overview.place(relx=0.172,
                                    rely=0.75,
                                    relwidth=0.23,
                                    relheight=0.05)

experimental_products_label_overview = CTkLabel(overview_frame_analytics_frame,
                                        text = "🧪 Experimental: ",
                                                font=("Helvetica",18))

experimental_products_label_overview .place(relx=0.17,
                                    rely=0.82,
                                    relwidth=0.23,
                                    relheight=0.05)


low_performers_label_overview = CTkLabel(overview_frame_analytics_frame,
                                        text = "📉 Low Performers: ",
                                         font=("Helvetica",18))

low_performers_label_overview .place(relx=0.18,
                                    rely=0.89,
                                    relwidth=0.23,
                                    relheight=0.05)



# i need to create sublabels for the number of the things.


star_products_sub_label_overview = CTkLabel(overview_frame_analytics_frame,
                                        text = "67",
                                        font=("Arial",16))


star_products_sub_label_overview.place(relx=0.37,
                                    rely=0.68,
                                    relwidth=0.1,
                                    relheight=0.05)

cash_cows_sub_label_overview = CTkLabel(overview_frame_analytics_frame,
                                        text = "67",
                                        font=("Arial",16))


cash_cows_sub_label_overview.place(relx=0.37,
                                    rely=0.75,
                                    relwidth=0.1,
                                    relheight=0.05)

experimental_products_sub_label_overview = CTkLabel(overview_frame_analytics_frame,
                                        text = "67",
                                        font=("Arial",16))


experimental_products_sub_label_overview.place(relx=0.37,
                                    rely=0.82,
                                    relwidth=0.1,
                                    relheight=0.05)

low_performers_sub_label_overview = CTkLabel(overview_frame_analytics_frame,
                                        text = "67",
                                        font=("Arial",16))


low_performers_sub_label_overview.place(relx=0.37,
                                    rely=0.89,
                                    relwidth=0.1,
                                    relheight=0.05)


#i need the best product's details to be displayed ig and its performance score.

best_product_details_label = CTkLabel(overview_frame_analytics_frame,
                                        text = "Best Product Details",
                                        font=("Helvetica",20, "bold"))


best_product_details_label.place(relx=0.45,
                                 rely=0.591,
                                 relwidth=0.23,
                                 relheight=0.1)

#label and sublabels
best_product_score_label = CTkLabel(overview_frame_analytics_frame,
                                        text = "Score: ",
                                        font=("Arial",18))

best_product_score_label.place(     relx=0.429,
                                    rely=0.68,
                                    relwidth=0.23,
                                    relheight=0.05)


best_product_score_sub_label_overview = CTkLabel(overview_frame_analytics_frame,
                                        text = "67",
                                        font=("Arial",16))


best_product_score_sub_label_overview.place(relx=0.58,
                                    rely=0.68,
                                    relwidth=0.1,
                                    relheight=0.05)

best_product_category_label = CTkLabel(overview_frame_analytics_frame,
                                        text = "Category: ",
                                        font=("Arial",18),
                                       height = 13)

best_product_category_label.place(     relx=0.442,
                                    rely=0.76,
                                    relwidth=0.23
                                    )

best_product_category_sub_label_overview = CTkLabel(overview_frame_analytics_frame,
                                        text = "67",
                                        font=("Arial",16))


best_product_category_sub_label_overview.place(relx=0.6,
                                    rely=0.75,
                                    relwidth=0.1,
                                    relheight=0.05)


best_product_suggestion_label = CTkLabel(overview_frame_analytics_frame,
                                        text = "Suggestion: ",
                                        font=("Arial",18),
                                         height = 13)

best_product_suggestion_label.place(     relx=0.45,
                                    rely=0.83,
                                    relwidth=0.23)

best_product_suggestion_sub_label = CTkLabel(overview_frame_analytics_frame,
                                        text = "Increase Production",
                                        font=("Arial",18),
                                         height = 13)

best_product_suggestion_sub_label.place(relx=0.61,
                                    rely=0.83,
                                    relwidth=0.25)









# suggestions

def open_suggestions_management():
    suggestions_frame.tkraise()

suggestions_button = CTkButton(home_frame,
                               command= open_suggestions_management,
                               text = "Suggestions",
                               width = 250,
                               height = 50,
                               font =("Arial", 20))

suggestions_button.pack(pady=(0,10))

# inside suggestions frame stuff
suggestions_title = CTkLabel(suggestions_frame,text = "Suggestions" , font =("Arial", 30))
suggestions_title.place(
                                relx=0,
                                rely=0.1,
                                relwidth=0.5,
                                relheight=0.1)


suggestions_close_button = CTkButton(suggestions_frame,
                                     command= go_back_to_home_function,
                                     text = "Back",
                                     width = 150,
                                     height = 35,
                                     font =("Arial", 13))

suggestions_close_button.place(
                                            relx=0.85,
                                            rely=0.85,
                                            relwidth=0.07,
                                            relheight=0.07)



app.mainloop()