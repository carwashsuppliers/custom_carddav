from odoo import http
from odoo.http import request, Response
import logging

_logger = logging.getLogger(__name__)

class CardDAVController(http.Controller):

    @http.route(['/carddav/<int:partner_id>.vcf'], type='http', auth='user', website=False)
    def serve_vcard(self, partner_id, **kwargs):
        """Serve a vCard file for a specific contact"""
        partner = request.env['res.partner'].sudo().browse(partner_id)
        if not partner:
            return Response("Contact not found", status=404)
        
        vcard_data = partner.generate_vcard()
        headers = [
            ('Content-Type', 'text/vcard'),
            ('Content-Disposition', f'attachment; filename="{partner.name}.vcf"')
        ]
        return Response(vcard_data, headers=headers)

    @http.route(['/carddav/contacts.vcf'], type='http', auth='user', website=False)
    def serve_all_vcards(self, **kwargs):
        """Serve all contacts as a single vCard file"""
        partners = request.env['res.partner'].sudo().search([('carddav_sync', '=', True)])
        if not partners:
            return Response("No contacts found", status=404)
        
        vcard_data = "\n".join(partner.generate_vcard() for partner in partners)
        headers = [
            ('Content-Type', 'text/vcard'),
            ('Content-Disposition', 'attachment; filename="contacts.vcf"')
        ]
        return Response(vcard_data, headers=headers)

    @http.route(['/carddav'], type='http', auth='user', website=False)
    def carddav_endpoint(self, **kwargs):
        """CardDAV discovery endpoint"""
        base_url = request.httprequest.host_url
        response_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
        <D:multistatus xmlns:D="DAV:">
            <D:response>
                <D:href>{base_url}carddav/</D:href>
                <D:propstat>
                    <D:prop>
                        <D:resourcetype>
                            <D:collection/>
                        </D:resourcetype>
                    </D:prop>
                    <D:status>HTTP/1.1 200 OK</D:status>
                </D:propstat>
            </D:response>
        </D:multistatus>
        """
        return Response(response_xml, content_type="application/xml", status=207)
