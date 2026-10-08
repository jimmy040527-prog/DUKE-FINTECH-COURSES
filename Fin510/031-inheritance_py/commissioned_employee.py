from salaried_employee import SalariedEmployee


class CommissionedEmployee(SalariedEmployee):
    def __init__(self, name, job_title, annual_pay_rate, period_gross_sales):
        super().__init__(name, job_title, annual_pay_rate)

        self.period_gross_sales = period_gross_sales
        
    @property
    def employee_type(self):
        return "commissioned"

    def calculate_pay(self):
        return (super().calculate_pay() + 0.05 * self.period_gross_sales)
