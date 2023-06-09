#calculate tax paid with given tax brackets, tax rates, and income

input1 = [0, 1000.0, 3000.0]
input2 = [0.1, 0.2, 0.3]
input3 = 2000

def tax_calculator(input1, input2, input3):
    ans = 0
    for i in range(0, len(input1)):
        try:
            if input3 < 0:
                break
            if input3 < input1[i+1]:
                tax_amount = input3 * input2[i]
            else:
                tax_amount = input1[i+1] * input2[i]
            ans += tax_amount
            input3 = input3 - input1[i+1]
        except:
            if input3 < input1[len(input1)-1]:
                tax_amount = input3 * input2[i]
            else:
                tax_amount = input1[len(input1)-1] * input2[i]
            ans += tax_amount
            input3 = input3 - input1[len(input1)-1]
    return ans

print(tax_calculator(input1, input2, input3))
