import sys
def get_percentages(notification):
    words = notification.split(" ")
    for word in words:
        if "%" in word:
            if word[:-1].replace(".", "").isdigit():
                return float(word[:-1])
    return None
def main():
    all_inputs = list(map(str.strip, sys.stdin.readlines()))
    store = list(map(int, all_inputs[0].split(" ")))
    money = int(all_inputs[-1])
    if money >= sum(store):
        return "true"
    for i in range(len(store)):
        percentage =  get_percentages(all_inputs[i + 1])
        if percentage is not None:
            if "lower" in all_inputs[i + 1]:
                money -= ((100 - percentage)*0.01)*store[i]
            elif "higher" in all_inputs[i + 1]:
                money -= ((100 + percentage)*0.01)*store[i]
        else:
            money -= store[i]
    
    return "true" if money >= 0 else "false"
    
sys.stdout.write(main())