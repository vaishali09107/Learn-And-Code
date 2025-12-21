class CustomerSearch:

    def __init__(self, customers):
        """ customers: list of customer objects or dictionaries """
        self.customers = customers

    def search_by_country(self, country: str):
        """ Returns customers matching the given country. """
        return self._search_customers(
            lambda customer: country in customer["country"]
        )

    def search_by_company_name(self, company_name: str):
        """ Returns customers matching the given company name. """
        return self._search_customers(
            lambda customer: company_name in customer["company_name"]
        )

    def search_by_contact_name(self, contact_name: str):
        """ Returns customers matching the given contact name. """
        return self._search_customers(
            lambda customer: contact_name in customer["contact_name"]
        )

    def _search_customers(self, filter_condition):
        """ Filters and sorts customers based on the given condition. """
        return sorted(
            filter(filter_condition, self.customers),
            key=lambda customer: customer["customer_id"]
        )

    def export_customers_to_csv(self, customers):
        """ Exports customer data to CSV format. """
        lines = []

        for customer in customers:
            line = (
                f'{customer["customer_id"]},'
                f'{customer["company_name"]},'
                f'{customer["contact_name"]},'
                f'{customer["country"]}'
            )
            lines.append(line)

        return "\n".join(lines)
