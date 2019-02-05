
from odoo import fields, models, _, api
from odoo.exceptions import ValidationError



class EagleeducationApplication(models.Model):
    _name = 'eagleeducation.pplication'
    _inherit = ['mail.thread']
    _description = 'Applications for the admission'
    _order = 'id desc'

    name = fields.Char(string='Name', required=True, help="Enter Name of Student")
    name_b = fields.Char("নাম")

    student_id = fields.Char('Student Id')
    level = fields.Integer('Level')
    section = fields.Char('Section')
    group = fields.Char('Group')
    roll_no = fields.Integer('Roll No')
    Batch = fields.Char('Batch')

    student_category = fields.Selection([('I', "Internal"),
                                         ('E', "External")], 'Category')
    #prev_school = fields.Many2one('education.institute', string='Previous Institution',
                                  help="Enter the name of previous institution")
    image = fields.Binary(string='Image', help="Provide the image of the Student")
    #academic_year_id = fields.Many2one('education.academic.year', related='register_id.academic_year',
                                       #string='Academic Year',
                                       #help="Choose Academic year for which the admission is choosing")
    #medium = fields.Many2one('education.medium', string="Medium", required=True, default=1,
                             #help="Choose the Medium of class, like Bengali,English etc")

    application_date = fields.Datetime('application Date',default=lambda self: fields.datetime.now()) #, default=fields.Datetime.now, required=True
    application_no = fields.Char(string='Application  No', required=True, copy=False, readonly=True,
                       index=True, default=lambda self: _('New'))
    #company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.user.company_id)
    email = fields.Char(string="student Email", help="Enter E-mail id for contact purpose")
    phone = fields.Char(string="student Phone", help="Enter Phone no. for contact purpose")
    mobile = fields.Char(string="Student Mobile", help="Enter Mobile num for contact purpose")
    #nationality = fields.Many2one('res.country', string='Nationality', ondelete='restrict',default=19,
                                  #help="Select the Nationality")

    house = fields.Char(string='House No. or Village ', help="Enter the House No. or Village Name")
    road = fields.Char(string='Road No. or Post Office', help="Enter the Road No. or Post Office")
    city = fields.Char(string='City or Police Station', help="Enter the City or Police Station")
    dist = fields.Char(string='District', help="Enter the District name")
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict',default=19,
                                 help="Select the Country")

    is_same_address = fields.Boolean(string="Permanent Address same as above", default=True,
                                     help="Tick the field if the Present and permanent address is same")
    village = fields.Char(string='Village', help="Enter the Village Name")
    post_offce = fields.Char(string='Post Office', help="Enter the Post Office")
    polie_station = fields.Char(string='Police Station', help="Enter the Police Station")
    dist = fields.Char(string='District', help="Enter the District name")
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict',default=19,
                                 help="Select the Country")

    date_of_birth = fields.Date(string="Date Of birth", required=True, help="Enter your DOB")

    #guardian_relation = fields.Many2one('gurdian.student.relation', string="Relation to Guardian",  required=True,
                                        #help="Tell us the Relation toyour guardian")
    #### guardian Details
    guardian_name = fields.Char(string="guardian's Name", help="Proud to say my guardian is")
    guardian_mobile = fields.Char(string="guardian's Mobile No", help="guardian's Mobile No")

    #### Father Details
    father_name = fields.Char(string="Father's Name", help="Proud to say my father is",required=True)
    father_name_b = fields.Char(string="বাবার নাম", help="Proud to say my father is")
    father_NID = fields.Char(string="Father's NID", help="Father's NID")
    father_mobile = fields.Char(string="Father's Mobile No", help="Father's Mobile No")
    car_no = fields.Char(string="Car No", help="Car No")

    #### Mother Details
    mother_name = fields.Char(string="mother's Name", help="Proud to say my mother is",required=True)
    mother_name_b = fields.Char(string="মা এর নাম", help="Proud to say my mother is")
    mother_NID = fields.Char(string="mother's NID", help="mother's NID")
    mother_mobile = fields.Char(string="mother's Mobile No", help="mother's Mobile No")

    #religion_id = fields.Many2one('religion.religion', string="Religion", help="My Religion is ")

    #class_id = fields.Many2one('education.class.division', string="Class")
    #active = fields.Boolean(string='Active', default=True)

    #document_count = fields.Integer(compute='_document_count', string='# Documents')
    #verified_by = fields.Many2one('res.users', string='Verified by', help="The Document is verified by")
    #reject_reason = fields.Many2one('application.reject.reason', string='Reject Reason',
                                    #help="Application is rejected because")

    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
                              string='Gender', required=True, default='male', track_visibility='onchange',
                              help="Your Gender is ")
    blood_group = fields.Selection([('a+', 'A+'), ('a-', 'A-'), ('b+', 'B+'), ('o+', 'O+'), ('o-', 'O-'),
                                    ('ab-', 'AB-'), ('ab+', 'AB+')],
                                   string='Blood Group', track_visibility='onchange',
                                   help="Your Blood Group is ")

    #state = fields.Selection([('draft', 'Draft'), ('verification', 'Verify'),
                              #('approve', 'Approve'), ('reject', 'Reject'), ('done', 'Done')],
                             #string='State', required=True, default='draft', track_visibility='onchange')

    _sql_constraints = [
        ('unique_student_id', 'unique(student_id)', 'Student Id must be unique'),
    ]

    @api.model
    def create(self, vals):
        """Overriding the create method and assigning the the sequence for the record"""
        if vals.get('application_no', _('New')) == _('New'):
            vals['application_no'] = self.env['ir.sequence'].next_by_code('eagleeducation.application') or _('New')
        res = super(EagleeducationApplication, self).create(vals)
        return res