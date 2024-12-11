# Calculate compound interest

def compound(init, monthly, time, interest):
    interest = interest / 100
    result = init * ((1 + interest / 12)**(12*time)) + monthly * (((1 + interest / 12)**(12*time)) - 1) / (interest / 12)
    return int(result)

try:
    init = float(input('--> Your initial investment: '))
    monthly = float(input('--> Your monthly investment: '))
    time = float(input('--> How long will you invest (in years): '))
    interest = float(input('--> Interest rate: '))
    print(f'${compound(init, monthly, time, interest)}')
except ValueError:
    print('incorrect input')

