
'''
Program Description:
    This program calculates the tax liability, refunds, or additional tax owed by the user based on their income, deductions, and credits.

Inputs:
    - Filing status
    - Income sources (wages, freelance, unemployment)
    - Deductions and credits (education, student loan, charitable donations)
    - Federal tax withheld
    - Estimated tax payments

Outputs:
    - Filing status
    - Total taxable income
    - Total deductions
    - Total tax owed
    - Refund or additional tax owed

Author: Jazlynn Bailey
Date: October 13, 2024
'''

'''
Step 1: Filing Status
The code for determining filing status is perfect except for indentation.
Using the control flow diagram linked in the instructions, correct the following code by 
changing indentation ONLY. Feel free to add whitespace (blank lines) for better readability.
'''

filing_status = ''
is_married = input('Are you married? (Y/N) ')
if is_married.upper() == 'Y':
    is_filing_separately = input('Are you filing separately from your spouse? (Y/N) ')
    if is_filing_separately.upper() == 'Y':
        filing_status = 'Married filing separately'
    else:
        filing_status = 'Married filing jointly'
else:
    is_spouse_deceased = input('Did your spouse pass away within the last two years? (Y/N) ')
    if is_spouse_deceased.upper() == 'Y':
        filing_status = 'Qualifying surviving spouse'
    else:
        has_dependents = input('Do you support any dependents? (Y/N) ')
        if has_dependents.upper() == 'Y':
            paid_more_than_half = input('Did you pay more than half the cost of keeping up a home? (Y/N) ')
            if paid_more_than_half.upper() == 'Y':
                filing_status = 'Head of household'
            else:
                filing_status = 'Single'
        else:
            filing_status = 'Single'

print(f'Your filing status is: {filing_status}', end='\n\n')


'''
Step 2: Income
The code for determining income is perfect except for indentation.
Using the control flow diagram linked in the instructions, correct the following code
by correcting indentation ONLY. Feel free to add whitespace (blank lines) for better readability.
'''

total_income = 0

#ask about wage income
earned_wages = input('Did you earn wages/salary from a job? (Y/N) ')
if earned_wages.upper() == 'Y':
    wages_amount = float(input('How much did you earn in wages/salary? $'))
    total_income += wages_amount

#ask about freelance income
earned_freelance = input('Did you have any freelance or self-employment income? (Y/N) ')
if earned_freelance.upper() == 'Y':
    freelance_amount = float(input('How much did you earn from freelance or self-employment? $'))
    total_income += freelance_amount

#ask about unemployment benefits
received_unemployment = input('Did you receive unemployment benefits? (Y/N) ')
if received_unemployment.upper() == 'Y':
    unemployment_amount = float(input('How much did you receive in unemployment benefits? $'))
    total_income += unemployment_amount

#display the total income
print(f'Your total taxable income is: ${total_income:.2f}', end='\n\n')


'''
Step 3: Deductions and Credits
The code for calculating deductions and credits is below. Using this control flow diagram linked in 
the instructions, your task is to calculate total_credits and total_deductions. That is, your task 
is to write code for the first three decisions (order matters). 
The final decision (total_deductions > standard_deduction) is given to you.  
'''

education_credit = 1000
student_loan_deduction = 2500
total_deductions = 0
total_credits = 0

is_student = input('Are you a full-time student? (Y/N) ')
if is_student.upper() == 'Y':
    total_credits += education_credit  #education credit

paid_student_loan_interest = input('Did you pay student loan interest? (Y/N) ')
if paid_student_loan_interest.upper() == 'Y':
    total_deductions += student_loan_deduction  #student loan deduction

made_charitable_donations = input('Did you make charitable donations this year? (Y/N) ')
if made_charitable_donations.upper() == 'Y':
    donation_amount = float(input('How much did you donate to charity? $'))
    total_deductions += donation_amount  #donation amount to total deductions

standard_deduction = 12550

if total_deductions > standard_deduction:
    print(f'You qualify for itemized deductions totaling: ${total_deductions:.2f}')
else:
    total_deductions = standard_deduction
    print(f'You qualify for the standard deduction of: ${total_deductions:.2f}')

print(f'Your total deductions are: ${total_deductions:.2f}')
print(f'Your total tax credits are: ${total_credits:.2f}', end='\n\n')


'''
Step 4: Taxes Owed
The code for calculating the first tax bracket is given to you:
10% on income up to $10,000
12% on income from $10,001 to $40,000
22% on income over $40,000

Your task is to calculate the second tax bracket when filing status is Married filing jointly:
10% on income up to $20,000
12% on income from $20,001 to $80,000
22% on income over $80,000
'''

#calculate taxable income
taxable_income = total_income - total_deductions
if taxable_income < 0:
    taxable_income = 0

tax_owed = 0

#tax brackets for users NOT filing jointly
if filing_status != 'Married filing jointly':
    if taxable_income <= 10000:
        tax_owed = taxable_income * 0.10
    elif taxable_income <= 40000:
        tax_owed = 10000 * 0.10 + (taxable_income - 10000) * 0.12
    else:
        tax_owed = 10000 * 0.10 + 30000 * 0.12 + (taxable_income - 40000) * 0.22

#tax brackets for users filing jointly
else:
    if taxable_income <= 20000:
        tax_owed = taxable_income * 0.10
    elif taxable_income <= 80000:
        tax_owed = 20000 * 0.10 + (taxable_income - 20000) * 0.12
    else:
        tax_owed = 20000 * 0.10 + 60000 * 0.12 + (taxable_income - 80000) * 0.22

#subtract total credits from tax owed
tax_owed -= total_credits
if tax_owed < 0:
    tax_owed = 0


print(f'Your taxable income is: ${taxable_income:.2f}')
print(f'Your total tax owed is: ${tax_owed:.2f}', end='\n\n')



'''
STEP 5: Refund or Payment Due
'''

#ask how much federal tax was withheld
federal_tax_withheld = float(input('How much federal tax was withheld from your paycheck? $'))

#ask if the user made estimated tax payments and get the amount
paid_estimated_tax_payment = input('Did you make any estimated tax payments? (Y/N) ')

estimated_tax_payments = 0
if paid_estimated_tax_payment.upper() == 'Y':
    estimated_tax_payments = float(input('How much did you pay in estimated tax payments? $'))

#calculate total payments
total_payments = federal_tax_withheld + estimated_tax_payments

#compare total payments with tax owed
if total_payments < tax_owed:
    additional_tax_owed = tax_owed - total_payments
    print(f'You owe an additional ${additional_tax_owed:.2f} in taxes.', end='\n\n')
else:
    refund_due = total_payments - tax_owed
    print(f'You are due a refund of ${refund_due:.2f}.', end='\n\n')



'''
Step 6: Final Report
Do NOT change anything in the print statements.
'''

print("--- Tax Summary Report ---")
print(f"Filing Status: {filing_status}")
print(f"Total Income: ${total_income:.2f}")
print(f"Total Deductions: ${total_deductions:.2f}")
print(f"Tax Owed: ${tax_owed:.2f}")
print(f"Total Payments Made: ${total_payments:.2f}")

if total_payments < tax_owed:
    print(f"You owe an additional ${additional_tax_owed:.2f} in taxes")
else:
    print(f"You are due a refund of ${refund_due:.2f}")


