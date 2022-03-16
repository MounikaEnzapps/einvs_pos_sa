from odoo import fields, models
import werkzeug.urls

try:
    import qrcode
except ImportError:
    qrcode = None

class NewClass(models.Model):
    _inherit = 'pos.order'


    qr_code_image = fields.Binary("QR Code", attachment=True)
    decoded_data = fields.Char(string="Decoded Data")
    debit_note = fields.Boolean(default=False)
    credit_note = fields.Boolean(default=False)
    qr_image = fields.Binary(string="QR Image")
    datetime_field = fields.Datetime(string="Create Date", default=lambda self: fields.Datetime.now())

    def enzapps_custom_call_image(self):
        rec = self.env['pos.order'].search([('pos_reference', '=', self.id)])
        return rec.qr_image


    # def enzapps_custom_call(self):
    #
    #
    #
    #     rec = self.env['pos.order'].search([('pos_reference','=',self.id)])
    #     print('dfdsfdfgfdgfdgfdhfghgf',self)
    #
    #     qr = qrcode.QRCode(
    #         version=1,
    #         error_correction=qrcode.constants.ERROR_CORRECT_L,
    #         box_size=20,
    #         border=4,
    #     )
    #
    #     leng = len(rec.company_id.name)
    #     company_name = rec.company_id.name
    #     if 42 > leng:
    #         for r in range(42 - leng):
    #             if len(company_name) != 42:
    #                 company_name += ' '
    #             else:
    #                 break
    #     else:
    #         if 42 < leng:
    #             company_name = company_name[:42]
    #     vat_leng = len(rec.company_id.vat)
    #     vat_name = rec.company_id.vat
    #     if 17 > vat_leng:
    #         for r in range(15 - vat_leng):
    #             if len(vat_name) != 15:
    #                 vat_name += ' '
    #             else:
    #                 break
    #     else:
    #         if 17 < leng:
    #             vat_name = vat_name[:17]
    #
    #     amount_total = str(rec.amount_total)
    #     amount_leng = len(str(rec.amount_total))
    #     if len(amount_total) < 17:
    #         for r in range(17 - amount_leng):
    #             if len(amount_total) != 17:
    #                 amount_total += ' '
    #             else:
    #                 break
    #
    #     tax_leng = len(str(15.00))
    #     amount_tax_total = str(rec.amount_tax)
    #     if len(amount_tax_total) < 17:
    #         for r in range(17 - tax_leng):
    #             if len(amount_tax_total) != 17:
    #                 amount_tax_total += ' '
    #             else:
    #                 break
    #     from datetime import date, timedelta
    #     from  datetime import datetime
    #
    #     data = "*" + str(company_name) + "" + str(vat_name) + "" + str(datetime.today().date()) + "T" + str(
    #         rec.datetime_field.time()) + "Z" + "" + amount_total + "" + amount_tax_total
    #     import base64
    #     mou = base64.b64encode(bytes(data, 'utf-8'))
    #
    #     # rec.decoded_data = str(mou.decode())
    #     #
    #     # qr = qrcode.QRCode(
    #     #     version=1,
    #     #     error_correction=qrcode.constants.ERROR_CORRECT_L,
    #     #     box_size=20,
    #     #     border=4,
    #     # )
    #     # data_im = str(mou.decode())
    #     # qr.add_data(data_im)
    #     # qr.make(fit=True)
    #     # img = qr.make_image()
    #     #
    #     # import io
    #     # import base64
    #     #
    #     # temp = io.BytesIO()
    #     # img.save(temp, format="PNG")
    #     # qr_image = base64.b64encode(temp.getvalue())
    #     # rec.qr_code_image = qr_image
    #     #
    #     # return str(mou.decode())
    #     # data = rec.pos_reference + '\n' + rec.name + '\n' + rec.session_id.name + '\n' + 'Amount:' + str(
    #     #     rec.amount_total)
    #
    #     qr.add_data(mou.decode())
    #     qr.make(fit=True)
    #     img = qr.make_image()
    #
    #     import io
    #     import base64
    #
    #     temp = io.BytesIO()
    #     img.save(temp, format="PNG")
    #     qr_image = base64.b64encode(temp.getvalue())
    #     rec.qr_code_image = qr_image
    #     print(rec.qr_code_image)
    #     print(rec.qr_code_image.decode())
    #     print(mou.decode())
    #
    #     return str(mou.decode())

    def enzapps_custom_call(self):
        rec = self.env['pos.order'].search([('pos_reference', '=', self.id)])
        # leng = len(rec.company_id.name)
        # company_name = rec.company_id.name
        # if 42 > leng:
        #     for r in range(42 - leng):
        #         if len(company_name) != 42:
        #             company_name += ' '
        # #         else:
        # #             break
        # # else:
        # #     if 42 < leng:
        # #         company_name = company_name[:42]
        # # vat_leng = len(rec.company_id.vat)
        # # vat_name = rec.company_id.vat
        # # if 17 > vat_leng:
        # #     for r in range(15 - vat_leng):
        # #         if len(vat_name) != 15:
        # #             vat_name += ' '
        # #         else:
        # #             break
        # # else:
        # #     if 17 < leng:
        # #         vat_name = vat_name[:17]
        # #
        # # amount_total = str(rec.amount_total)
        # # amount_leng = len(str(rec.amount_total))
        # # if len(amount_total) < 17:
        # #     for r in range(17 - amount_leng):
        # #         if len(amount_total) != 17:
        # #             amount_total += ' '
        # #         else:
        # #             break
        # #
        # # tax_leng = len(str(rec.amount_tax))
        # # amount_tax_total = str(rec.amount_tax)
        # # if len(amount_tax_total) < 17:
        # #     for r in range(17 - tax_leng):
        # #         if len(amount_tax_total) != 17:
        # #             amount_tax_total += ' '
        # #         else:
        # #             break
        # # data = "*" + str(company_name) + "" + str(vat_name) + "" + str(self.invoice_date) + "T" + str(
        # #     self.datetime_field.time()) + "Z" + "" + amount_total + "" + amount_tax_total
        #
        # # data = ""+'Salah Hospital'+""+'31012239350000311123'+""+'2023-01-01'+"T"+str(rec.datetime_field.time())+""+str(200.00)+""+str(125.00)
        # data = ""+"BROTHERS GROUP   "+""+"300090000000003"+""+"2021-11-08"+"T"+"13:45:38"+""+"9.00"+""+"1.18"

        leng = len(rec.company_id.name)
        company_name = rec.company_id.name
        if 42 > leng:
            for r in range(42 - leng):
                if len(company_name) != 42:
                    company_name += ' '
                else:
                    break
        else:
            if 42 < leng:
                company_name = company_name[:42]
        vat_leng = len(rec.company_id.vat)
        vat_name = rec.company_id.vat
        if 17 > vat_leng:
            for r in range(15 - vat_leng):
                if len(vat_name) != 15:
                    vat_name += ' '
                else:
                    break
        else:
            if 17 < leng:
                vat_name = vat_name[:17]

        amount_total = str(rec.amount_total)
        amount_leng = len(str(rec.amount_total))
        if len(amount_total) < 17:
            for r in range(17 - amount_leng):
                if len(amount_total) != 17:
                    amount_total += ' '
                else:
                    break

        tax_leng = len(str(rec.amount_tax))
        amount_tax_total = str(rec.amount_tax)
        if len(amount_tax_total) < 17:
            for r in range(17 - tax_leng):
                if len(amount_tax_total) != 17:
                    amount_tax_total += ' '
                else:
                    break
        from datetime import datetime

        data = "*" + str(company_name) + "" + str(vat_name) + "" + str(datetime.today().date()) + "T" + str(
            rec.datetime_field.time()) + "Z" + "" + amount_total + "" + amount_tax_total

        import base64
        mou = base64.b64encode(bytes(data, 'utf-8'))
        rec.decoded_data = str(mou.decode())

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=20,
            border=4,
        )
        data_im = str(mou.decode())
        qr.add_data(data_im)
        qr.make(fit=True)
        img = qr.make_image()

        import io
        import base64

        temp = io.BytesIO()
        img.save(temp, format="PNG")
        qr_image = base64.b64encode(temp.getvalue())
        rec.sudo().qr_image = qr_image
        print(mou.decode())


        # return str(mou.decode())
        return str(rec.qr_image.decode())




