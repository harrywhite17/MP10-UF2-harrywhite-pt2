from odoo import fields, models, tools

class ReportComercialPropertyState(models.Model):
    _name = 'report.comercial.property.state'
    _description = "Report per Comercial i Estat de Propietat"
    _auto = False
    _rec_name = 'comercial'

    comercial = fields.Many2one('res.users', string='Comercial', readonly=True)
    state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled')
    ], string='Estat de la Propietat', readonly=True)
    total_price = fields.Float(string='Total Preu Ofertes', readonly=True)
    nombre_ofertes = fields.Integer(string="Nombre d'ofertes", readonly=True)

    def _select(self):
        return """
            row_number() over() as id,
            u.id as comercial,
            p.state as state,
            COALESCE(SUM(o.price), 0) as total_price,
            COUNT(o.id) as nombre_ofertes
        """

    def _from(self):
        return """
            estate_property p
            LEFT JOIN estate_property_offer o ON p.id = o.property_id
            LEFT JOIN res_users u ON p.salesman_id = u.id
        """

    def _group_by(self):
        return """
            u.id, p.state
        """

    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""
            CREATE or REPLACE VIEW %s as
            SELECT %s
            FROM %s
            GROUP BY %s
        """ % (self._table, self._select(), self._from(), self._group_by()))