import requests
from datetime import datetime
import webbrowser


class HabitTracker:
    def __init__(self):
        self.GraphID = None
        self.UserName = None
        self.Token = None

    def update_user(self):
        self.UserName = input("Enter your User name\n")
        former_token = input("Please Enter Your Token/Password\n")
        new_token = input("Please Enter your new Password/token\n")
        API_ENDPOINT = f"https://pixe.la/v1/users/{self.UserName}"
        latest_user_details = {
            "newToken": new_token,
        }
        Key = {
            "X-USER-TOKEN": former_token,
        }
        response = requests.put(url=API_ENDPOINT, json=latest_user_details, headers=Key)
        print(response.text)

    def create_user(self):
        self.Token = input("Enter a Password/token for your account\n")
        self.UserName = input("Enter Your User Name\n")
        API_ENDPOINT = "https://pixe.la/v1/users"
        new_user_parameters = {
            "token": self.Token,
            "username": self.UserName,
            "agreeTermsOfService": "yes",
            "notMinor": "yes",
        }
        response = requests.post(url=API_ENDPOINT, json=new_user_parameters)
        print(response.text)

    def delete_user(self):
        self.UserName = input("Please Enter your user name \n")
        API_ENDPOINT = f"https://pixe.la/v1/users/{self.UserName}"
        self.Token = input("Please enter your token/Password \n")
        header_params = {
            "X-USER-TOKEN": self.Token,
        }
        "https://pixe.la/v1/users/"
        response = requests.delete(url=API_ENDPOINT, headers=header_params)
        print(response.text)

    def view_profile(self):
        self.UserName = input("Please Enter your user name \n")
        profile_url = f"https://pixe.la/@{self.UserName}"
        webbrowser.open(profile_url)

    def post_pixel(self):
        self.UserName = input("Please Enter your user name \n")
        self.GraphID = input("Please Enter your Graph ID \n")
        self.Token = input("Please Enter your Password/Token \n")
        quantity = input("Please Specify the quantity to be registered today")
        API_ENDPOINT = f"https://pixe.la/v1/users/{self.UserName}/graphs/{self.GraphID}"
        key = {
            "X-USER-TOKEN": self.Token,
        }
        json_parameters = {
            "date": f"{datetime.today().strftime('%Y%m%d')}",
            "quantity": quantity,
        }
        response = requests.post(url=API_ENDPOINT, json=json_parameters, headers=key)
        print(response.text)

    def create_graph(self):
        self.UserName = input("Please Enter your user name \n")
        self.GraphID = input("Please Enter your Graph ID \n")
        self.Token = input("Please Enter your Password/Token \n")
        GraphName = input("Please Enter the name of the graph \n")
        unit = input("Please enter a unit of the quantity recorded in "
                     "the pixelation graph. Ex. commit, kilogram, calory\n")
        datatype = input("Enter the the type of quantity to be handled in the graph. "
                         "Only int or float are supported.\n")
        color = input("Enter your desired pixel color. Ex. shibafu (green), momiji (red), sora (blue), ichou (yellow), "
                      "ajisai (purple) and kuro (black)\n")
        API_ENDPOINT = f"https://pixe.la/v1/users/{self.UserName}/graphs"
        json_parameters = {
            "id": self.GraphID,
            "name": GraphName,
            "unit": unit,
            "color": color,
            "type": datatype,
        }
        key_header = {
            "X-USER-TOKEN": self.Token,
        }
        response = requests.post(url=API_ENDPOINT, json=json_parameters, headers=key_header)
        print(response.text)


new_user = HabitTracker()
user_choice = input("For new pixela account press 1;\nfor new graph press 2;\nTo update user details press 3;\n"
                    "To delete your account press 4;\nTo view your profile press 5;\nTo post pixel press 6\n").strip()
if user_choice == "1":
    new_user.create_user()
elif user_choice == "2":
    new_user.create_graph()
elif user_choice == "3":
    new_user.update_user()
elif user_choice == "4":
    new_user.delete_user()
elif user_choice == "5":
    new_user.view_profile()
elif user_choice == "6":
    new_user.post_pixel()

