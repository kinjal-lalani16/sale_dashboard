from odoo import models
from datetime import date, timedelta


class SaleOrder(models.Model):

    _inherit = "sale.order"

# '''This method will return last month sale report(Total confirm sale order
#       toatal amount, total paid invoices, most sold products)'''

    def sale_count(self):
        print('helllo')
        confirm_order = self.env['sale.order'].search([('state', '=', 'sale')])
        invoices = self.env['account.move'].search([(
            'invoice_payment_state', '=', 'paid'
        )])
        paid_invoice_count = 0
        confirm_count = 0
        total_amount = 0
        product_dict = {}
        product_list = []

        for invoice in invoices:
            if invoice.invoice_date.month == date.today().month - 1:
                paid_invoice_count += 1

        for order in confirm_order:
            if order.date_order.month == date.today().month - 1:
                confirm_count += 1
                total_amount += order.amount_total
                for product in order.order_line:
                    if product.product_id.name in product_dict:
                        product_dict[product.product_id.name]['qty'] += product.product_uom_qty
                    else:
                        product_dict[product.product_id.name] = {
                            'qty': product.product_uom_qty,
                            'uom': product.product_uom.name
                        }
        for product in product_dict.items():
            if product[1].get('qty') > 15:
                product_list.append({
                    'name': product[0],
                    'qty': product[1].get('qty'),
                    'uom': product[1].get('uom')
                })
        dashboard_details = {
            'confirm_count': confirm_count,
            'total_amount': total_amount,
            'paid_invoice_count': paid_invoice_count,
            'product_list': product_list
        }
        return dashboard_details
