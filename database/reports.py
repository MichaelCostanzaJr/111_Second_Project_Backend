from app.database import get_db

def output_formatter(results):
    out = []
    for result in results:
        vehicle = {}
        vehicle["id"] = result[0]
        vehicle["first_name"] = result[1]
        vehicle["last_name"] = result[2]
        vehicle["hobbies"] = result[3]
        vehicle["active"] = result[4]
        out.append(user)
    return out