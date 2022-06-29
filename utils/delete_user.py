import requests

URL = "http://127.0.0.1:5000/users"

def delete_user(id):
    deactivate = {
        "id" = ()

    }

    response = requests.delete(URL, json=deactivate)
    if response.status_code == 204:
        print("User successfully deleted")
    else:
        print("Error: User was not deleted.")


# if the script is directly executed from the terminal
if __name__ == "__main__":
    print()
    print("DELETE USER")
    print("-" * 20)
    id = input("id: ")
    delete_user(id)