import datetime
from Product import Product
from SalesRecord import SalesRecord
from DatabaseManager import DatabaseManager

class CoreSystem:
    def __init__(self):

        self.database = DatabaseManager()

    def display_products(self):

        products = self.database.get_all_products()#works, no need for debugging
        for i in range(0,len(products)):
            product = products[i]
            print(product.name , product.selling_price , product.cost)

    def get_product_ID_by_name(self,name):

        products = self.database.get_all_products()
        for i in products:
            if i.name == name:
                return i.product_ID

    def get_product_name_by_ID (self, product_ID):
        products = self.database.get_all_products()
        for i in products:
            if i.product_ID == product_ID:
                return i.name

        print("Could not find product with PID:", product_ID)


    def get_product_price_by_name (self,name):
        products = self.database.get_all_products()
        for i in products:
            if i.name == name:
                return i.selling_price

    def get_product_cost_by_name (self,name):
        products = self.database.get_all_products()
        for i in products:
            if i.name == name:
                return i.cost

    def get_all_products (self):
        products = self.database.get_all_products()
        return products

    def get_all_sales_records (self):
        sales_records = self.database.get_all_sales_records()
        return sales_records

    def get_quantity_by_product_ID (self,product_ID):

        sales_records = self.database.get_all_sales_records()

        for i in sales_records:
            if i.product_ID == product_ID:
                return i.quantity

    def get_date_by_product_ID (self, product_ID):

        sales_records = self.database.get_all_sales_records()

        for i in sales_records:
            if i.product_ID == product_ID:
                return i.date

    def get_all_product_names (self):
        product_names = []
        all_products = self.get_all_products()

        for i in all_products:
            product_names.append(i.name)

        return product_names


    def get_no_of_products (self):

        product_names = self.get_all_product_names()

        return len(product_names)




    def get_monthly_sales(self,product_ID,month):
        # works, no need of logical debugging
        sales_records = self.database.get_all_sales_records()

        monthly_sales = 0

        for i in sales_records:
            if i.product_ID == product_ID:
                finding_month = i.date.split("-")
                if int(finding_month[1]) == month:
                        monthly_sales = monthly_sales + i.quantity
        return monthly_sales

    def get_monthly_sales_for_all_products(self,month): #this shit also works, need to print it
        sales_values = [] # resetting the list everytime so it won't accumulate it

        products = self.database.get_all_products()

        for i in products:
            sales = self.get_monthly_sales(i.product_ID,month)
            sales_values.append(sales)

        return sales_values

    def get_total_monthly_profit(self,product_ID,month):#works, but need to use print to print the returned value and product ID nonsense
        total_month_profit = 0

        products = self.database.get_all_products()

        for i in products:
            if i.product_ID == product_ID:
                profit_per_unit = i.get_profit_per_unit()
                total_month_profit = (self.get_monthly_sales(product_ID,month) * (profit_per_unit) )

        return  total_month_profit

    def get_total_monthly_profit_list_for_all_products(self,month): #works, need to print it and product ID fix

        total_monthly_profit = []

        products = self.database.get_all_products()

        for i in products:
            profit = self.get_total_monthly_profit(i.product_ID,month)
            total_monthly_profit.append(profit)

        return total_monthly_profit

    def get_margin_list (self): #works, need to print it
        margins = [] #resetting the list

        products = self.database.get_all_products()

        for i in products:
            margin = i.get_profit_margin()
            margins.append(margin)
        return margins

    def calculate_performance_score(self,product_ID,month): # cant verify the math, but upon print it works

        #for normalization purpose the function needs to be called every single time
        # performance score = (0.3 * sales volume) + (0.3 * profit margins) + (0.4 * total monthly profit)

        list_total_profit = self.get_total_monthly_profit_list_for_all_products(month)
        list_margins = self.get_margin_list()
        list_monthly_sales = self.get_monthly_sales_for_all_products(month)

        #initializing
        sales_value = 0
        profit_value = 0
        margin_value = 0

        products= self.database.get_all_products()

        for i in range (0,len(products)):
            current_product = products[i]
            # this will match the indices match between all the lists
            if current_product.product_ID == product_ID:
                sales_value = list_monthly_sales[i]
                margin_value = list_margins[i]
                profit_value = list_total_profit[i]

        if len(list_monthly_sales) == 0:
            return 0
        normalized_sales_denominator = (max(list_monthly_sales) - min(list_monthly_sales))

        if normalized_sales_denominator == 0 :
            normalized_sales = 0
        else:
            normalized_sales = ((sales_value - min(list_monthly_sales)) / normalized_sales_denominator)


        if len(list_total_profit) == 0:
            return 0
        normalized_profit_denominator = (max(list_total_profit) - min(list_total_profit))

        if normalized_profit_denominator == 0 :
            normalized_profit = 0
        else:
            normalized_profit = ((profit_value - min(list_total_profit)) / normalized_profit_denominator)


        if len(list_margins) == 0:
            return 0
        normalized_margin_denominator = (max(list_margins) - min(list_margins))

        if normalized_margin_denominator == 0:
            normalized_margin = 0
        else:
            normalized_margin = ((margin_value - min(list_margins)) / normalized_margin_denominator)


        weighted_performance_score = ((0.3* normalized_margin) + (0.3* normalized_sales) + (0.4 * normalized_profit))

        return round(weighted_performance_score,2)


    def categorize_products(self,month): #works, but printing the list needs to change, and cant verify math.

        list_for_categorization = []

        products = self.database.get_all_products()

        for i in range (0,len(products)):
            current_product = products[i]
            performance_score = self.calculate_performance_score(current_product.product_ID, month)
            product_performance_score = (current_product,performance_score)
            list_for_categorization.append(product_performance_score)

        #used that lambda thing to sort products based on performance score in descending order
        sorted_list_categorization = sorted(list_for_categorization,reverse=True,key = lambda x :x[1])
        no_of_scores = len(sorted_list_categorization) // 4
        if no_of_scores == 0:
            no_of_scores = 1

        #ranking based on percentile. Since the list is sorted, the top 25% will be the best product
        #since the list is sorted on performance score it will work. 

        for i in range(0,len(sorted_list_categorization)):
            current_product = sorted_list_categorization[i][0]
            current_performance_score = sorted_list_categorization[i][1]
            if i < no_of_scores :
                sorted_list_categorization [i] = (current_product.name,current_performance_score,"Star Product")
            elif i < (no_of_scores*2):
                sorted_list_categorization[i] = (current_product.name,current_performance_score,"Cash Cow")
            elif i < (no_of_scores* 3):
                sorted_list_categorization [i] = (current_product.name,current_performance_score,"Experimental Product")
            else:
                sorted_list_categorization [i] = (current_product.name,current_performance_score, "Low Performer")

        return sorted_list_categorization


    def generate_suggestions (self,month): # works, no issues. Changed from entire product to just product name
        sorted_list_categorization = self.categorize_products(month)
        suggestions = []

        for i in range(0,len(sorted_list_categorization)):
            current_product = sorted_list_categorization[i][0]
            current_performance_score = sorted_list_categorization[i][1]
            current_category = sorted_list_categorization[i][2]
            suggestion = ""
            if current_category == "Star Product":
                suggestion = (current_product,current_performance_score,current_category,"Increase Production")
            elif current_category == "Cash Cow":
                suggestion = (current_product, current_performance_score, current_category, "Maintain Production")
            elif current_category == "Experimental Product":
                suggestion = (current_product, current_performance_score, current_category, "Keep Experimenting")
            else:
                suggestion = (current_product, current_performance_score, current_category, "Reduce/Discontinue Production")

            suggestions.append(suggestion)

        return suggestions


    def display_rankings(self,month): # works, printing formatting just change a bit
        list_categorized = self.generate_suggestions(month)

        for i in range(0,len(list_categorized)):
            print (list_categorized[i][0], list_categorized[i] [1] ,list_categorized[i][2],list_categorized[i][3])


    def add_products(self,name, selling_price, cost):

        products = self.database.get_all_products()

        highest = 0

        for product in products:

            current = int(product.product_ID[3:])

            if current > highest:
                highest = current

        num = highest + 1

        product_ID = "PID" + str(num).zfill(3)

        product = Product(product_ID,name,selling_price,cost)

        self.database.add_product(product)



    def add_sales(self,product_ID,quantity):

        date = datetime.datetime.now()
        using_date = str(date).split(" ")
        date = using_date [0]

        sales_records = self.database.get_all_sales_records()
        highest = 0

        for record in sales_records:

            current = int(record.record_ID[3:])

            if current > highest:
                highest = current

        num = highest + 1

        record_ID = "RID" + str(num).zfill(3)

        sales_record = SalesRecord(record_ID,product_ID,date,quantity)

        self.database.add_sales_record(sales_record)






    def delete_product(self,product_ID):

        products = self.database.get_all_products()

        for i in products:
            if i.product_ID == product_ID:

                self.database.delete_product(product_ID)

                break

        self.database.delete_all_sales_records_by_product_ID(product_ID)


    def delete_one_sales_record(self,record_ID):

        sales_records = self.database.get_all_sales_records()

        for i in sales_records:
            if i.record_ID == record_ID:
                self.database.delete_sales_record(record_ID)

                break






    def get_total_profit (self):
        total_profit = 0

        sales_records = self.get_all_sales_records()
        products = self.get_all_products()

        for sales in sales_records:

            for product in products:

                if sales.product_ID == product.product_ID:

                    profit_per_unit = product.get_profit_per_unit()

                    total_profit = total_profit+ (profit_per_unit * sales.quantity)

                    break

        return total_profit

    def get_total_units_sold (self):
        total_units = 0

        sales_records = self.get_all_sales_records()

        for i in sales_records:
            total_units = total_units +i.quantity

        return total_units

    def get_best_product (self,month):
        categorized_products = self.categorize_products(month)
        return categorized_products [0][0]

    def get_best_product_score (self, month):
        categorized_products = self.categorize_products(month)
        return categorized_products[0][1]

    def get_best_product_category(self, month):
        categorized_products = self.categorize_products(month)
        return categorized_products[0][2]

    def get_best_product_suggestion(self, month):
        suggestions = self.generate_suggestions(month)
        return suggestions[0][3]






