

def display_produce():
    market1 = {"bananas", "oranges", "pineapples", "apples", "broccoli", "spinach", "lettuce"}
    market2 = {"broccoli", "potatoes", "lettuce", "beans", "apples", "grapes"}

    print("There are", (len(market1)), "at the first market and", (len(market2)), "products at the second market")

    both_markets = market1.union(market2)
    print("There are", (len(both_markets)), "unique items at the two markets")
    print("The products are: ")

    for x in both_markets:
        print(x)


def display_team(league):
    for name, team in league.items():
        print("The %s from %s" % (team, name))


def display_league():
    west_league = {"vancouver": "canucks", "edmonton": "oilers", "calgary": "flames"}
    east_league = {"toronto": "maple leafs", "ottawa": "senators", "montreal": "canadiens"}

    print("The west league: ")
    (display_team(west_league))
    print()

    print("The east league: ")
    (display_team(east_league))
    print()

    west_league["winnipeg"] = 'jets'

    print("After adding winnipeg... ")
    (display_team(west_league))
    print()

    west_league.update(east_league)

    print("After merging the two leagues: ")
    (display_team(west_league))


def get_total_population(this_dict):
    """Gets the total population
    :param this_dict is a dictionary"""
    total = 0
    for province in this_dict.values():
        total += province["population"]
        print(f"The total population of Canada is {total}")
        return


def get_capital_city(province_name, this_dict):
    """Retrieves the capital city of the province
    :param province_name: Name of the province
    :param this_dict: Dictionary containing province data
    :return: Name of capital city of province"""
    if province_name in this_dict:
        capital = this_dict[province_name]["capital"]
        print(f"The capital city of {province_name} is {capital}")
        return capital
    else:
        return ""


def get_largest_city(province_name, this_dict):
    """Retrieves the largest city of province
    :param province_name: Name of the province
    :param this_dict: Dictionary containing province data
    :return: Name of largest city in province"""
    if province_name in this_dict:
        largest = this_dict[province_name]["largest"]
        print(f"The largest city of {province_name} is {largest}")
        return largest
    else:
        return ""


def get_smallest_province(this_dict):
    """"""


def main():
    display_produce()
    display_league()

    canada = {
        "alberta": {"capital": "edmonton", "largest": "calgary", "population": 3645257},
        "ontario": {"capital": "toronto", "largest": "toronto", "population": 12851821},
        "quebec": {"capital": "quebec city", "largest": "montreal", "population": 7903001},
        "nova scotia": {"capital": "halifax", "largest": "halifax", "population": 921727},
        "new brunswick": {"capital": "fredericton", "largest": "saint john's", "population": 751171},
        "manitoba": {"capital": "winnipeg", "largest": "winnipeg", "population": 1208268},
        "prince edward island": {"capital": "charlottetown", "largest": " charlottetown", "population": 140204},
        "saskatchewan": {"capital": "regina", "largest": "saskatoon", "population": 1033381},
        "newfoundland and labrador": {"capital": "st. john's", "largest": "st. john's", "population": 514536},
        "yukon": {"capital": "whitehorse", "largest": "whitehorse", "population": 33897},
        "nunavut": {"capital": "iqaluit", "largest": "iqaluit", "population": 31906},
        "northwest territories": {"capital": "yellowknife", "largest": "yellowknife", "population": 41462},
        "british columbia": {"capital": "victoria", "largest": "vancouver", "population": 4400057}
    }

    get_total_population(canada)
    get_capital_city("british columbia", canada)
    get_largest_city("ontario", canada)


if __name__ == "__main__":
    main()
