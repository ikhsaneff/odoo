from odoo import models, fields, api
from odoo.http import request
import logging

logger = logging.getLogger(__name__)

class CustomHrApplicant(models.Model):
	_inherit="hr.applicant"