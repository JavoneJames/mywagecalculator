class EmployeeDetails:
    pay_rate = 10.5
    NIC = {'a': 0.1325, 'b': 0.071, 'f': 0.1325, 'h': 0.1325, 'i': 0.071, 'j': 0.0325, 'l': 0.0325, 'm': 0.1325,
           'v': 0.1325, 'z': 0.0325}
    upper_NIC = {'a': 0.0325, 'b': 0.0325, 'f': 0.0325, 'h': 0.0325, 'i': 0.0325, 'j': 0.0325, 'l': 0.0325, 'm': 0.0325,
                 'v': 0.0325, 'z': 0.0325}
    running_total = 0

    def __init__(self, hours, extra_pay, NIC_letter):
        self.hours = hours
        self.extra_pay = extra_pay
        self.NIC_letter = NIC_letter

    def pay_total(self):
        total = round((self.hours * self.pay_rate) + self.extra_pay, 2)
        return total

    def pay_deductions(self):
        estimate_total = self.pay_total()
        temp = 0
        if estimate_total < 1048.01:
            print("no nic to pay")
            return
        temp = self.primaryThresholdCalculation(estimate_total, temp)
        temp = self.secondaryThresholdCalculation(estimate_total, temp)
        total = estimate_total - temp
        print(temp)
        print(total)

    def primaryThresholdCalculation(self, estimate_total, temp):
        if estimate_total < 4189:
            deducted_total = estimate_total - 1048.01
            contribute = round(deducted_total * self.NIC.get(self.NIC_letter.lower(), 0), 2)
            temp = temp + contribute
        if estimate_total > 4189:
            deducted_total = 4189 - 1048.01
            contribute = round(deducted_total * self.NIC.get(self.NIC_letter.lower(), 0), 2)
            temp = temp + contribute
        return temp

    def secondaryThresholdCalculation(self, estimate_total, temp):
        if estimate_total > 4189:
            deducted_total = estimate_total - 4189
            contribute = round(deducted_total * self.upper_NIC.get(self.NIC_letter.lower(), 0), 2)
            temp = temp + contribute
        return temp

