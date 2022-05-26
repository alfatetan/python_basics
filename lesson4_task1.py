# The utilite calculates the staff wage

from sys import argv

def help():
    t = [
        "Welcome to the wage calculation!",
        "This utilite has several keys to use it",
        "-c or --cal - calculated the staff's wage",
        "   you need to use three params with this key:",
        "   hours, rate per hour, bonuses.",
        "   e.g.",
        "   python[3] lesson4_task1.py -c[--cal] [hour] [rate] [bonuses]",
        "\n",
        "-h or --help - this help",
        "\n",
        "-v or --version - the version of this utilite",

    ]
    for el in t:
        print(el)
    return

def cal():
    global argv
    name, key, hours, rate, bonus = argv
    try:
        hours, rate, bonus = float(hours), float(rate), float(bonus)
        print("The person earned $",(hours*rate)+bonus)
    except:
        print("Error! The params weren't the numbers!")
        return

def version():
    print("The wage calculator v.1.0")
    return

if __name__=="__main__":
    the_keys = {
        "-c": cal,
        "--cal": cal,
        "-v": version,
        "--version": version,
        "-h": help,
        "--help": help,
    }
    if argv[1] in the_keys.keys():
        the_keys[argv[1]]()
    else:
        print("Use the correct key or --help to read help")