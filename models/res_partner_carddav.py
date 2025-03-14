from odoo import models, fields

class ResPartnerCardDAV(models.Model):
    _inherit = "res.partner"

    carddav_sync = fields.Boolean(string="Sync with CardDAV", default=True)

    def generate_vcard(self):
        """Generate a vCard (.vcf) file with Company/Contact hierarchy and additional addresses"""

        is_company = self.is_company
        company_name = self.parent_id.name if self.parent_id else (self.name if is_company else "")

        address = f"{self.street};{self.city};{self.state_id.name if self.state_id else ''};{self.zip};{self.country_id.name if self.country_id else ''}"

        address_types = {
            'invoice': "ADR;TYPE=INVOICE",
            'delivery': "ADR;TYPE=DELIVERY",
            'other': "ADR;TYPE=OTHER",
            'followup': "ADR;TYPE=FOLLOWUP"
        }
        additional_addresses = []

        for child in self.child_ids.filtered(lambda c: c.type in address_types):
            formatted_address = f"{address_types[child.type]}:;;{child.street};{child.city};{child.state_id.name if child.state_id else ''};{child.zip};{child.country_id.name if child.country_id else ''}"
            additional_addresses.append(formatted_address)

        vcard_template = """BEGIN:VCARD
VERSION:3.0
{company_info}
FN:{name}
N:{last_name};{first_name};;;
ORG:{company_name}
TITLE:{job_title}
EMAIL;TYPE=WORK:{email}
TEL;TYPE=WORK:{phone}
TEL;TYPE=CELL:{mobile}
URL:{website}
ADR;TYPE=WORK:;;{address}
{additional_addresses}
END:VCARD"""

        return vcard_template.format(
            company_info="KIND:org" if is_company else "",
            name=self.name or "",
            first_name=self.name.split(" ")[0] if not is_company else "",
            last_name=" ".join(self.name.split(" ")[1:]) if not is_company else "",
            company_name=company_name or "",
            job_title=self.function or "",
            email=self.email or "",
            phone=self.phone or "",
            mobile=self.mobile or "",
            website=self.website or "",
            address=address,
            additional_addresses="\n".join(additional_addresses)
        )
