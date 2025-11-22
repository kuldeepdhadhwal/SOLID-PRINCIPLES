# Class responsible only for storing customer information
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

# Class responsible only for sending emails to customers
class EmailService:
    def send_email(self, customer, message):
        # In real code, email sending logic would go here
        print(f"Sending email to {customer.email}: {message}")

# Class responsible only for processing orders
class OrderService:
    def place_order(self, customer, order):
        # Here we would add order processing logic
        print(f"Placing order '{order}' for {customer.name}")

# Class responsible only for generating invoices for customers
class InvoiceService:
    def generate_invoice(self, customer, invoice):
        # Invoice generation logic goes here
        print(f"Generating invoice '{invoice}' for {customer.name}")

# Usage example:
customer = Customer("Alice", "alice@example.com")
email_service = EmailService()
order_service = OrderService()
invoice_service = InvoiceService()

# Each service performs its own responsibility independently
order_service.place_order(customer, "Product A")
invoice_service.generate_invoice(customer, "Invoice #123")
email_service.send_email(customer, "Thank you for your purchase!")

# If we need to change how emails are sent, we change only EmailService
# If order processing changes, only OrderService is updated
# Customer class only holds customer data; it doesn't do unrelated
