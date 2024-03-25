import ast


def get_route(route_config_path):
    with open(route_config_path) as file:
        content = file.read()

    route_list = ast.literal_eval(content)

    for point in route_list:
        point["lat"] = float(point["lat"])
        point["lng"] = float(point["lng"])

    return route_list
