'''Programming Set 1

This assignment will familiarize you with Python's basics.
'''

def savings(gross_pay, tax_rate, expenses):
    after_tax_pay=(gross_pay*(1-tax_rate))//1
    result=int(after_tax_pay-expenses)
    return result


def material_waste(total_material, material_units, num_jobs, job_consumption):
    total_material_consumed=num_jobs*job_consumption
    materials_remaining=total_material-total_material_consumed
    return f"{materials_remaining}{material_units}"


def interest(principal, rate, periods):
    simple_interest=principal*rate*periods
    final_amount=simple_interest+principal
    result=final_amount//1
    return int(result)