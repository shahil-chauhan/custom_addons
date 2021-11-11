# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, route


class Controller(http.Controller):
    @http.route("/create_employees", type="http", website=True, auth="public", csrf=False)
    def create_employees(self, **kw):
        employees = request.env["create.employees"].sudo().search([])
        states = request.env["res.country.state"].sudo().search([])
        countries = request.env["res.country"].sudo().search([])
        job_position = request.env["hr.job"].sudo().search([])
        return request.render(
            "create_employees.create_employees_template",
            {
                "employees": employees,
                "countries": countries,
                "states": states,
                "job_position": job_position,
            })

    @http.route("/employee_data", type="http", website=True, auth="user", csrf=False)
    def new_employee_create(self, **kw):
        name = kw.get("name")
        birth_date = kw.get("birth_date")
        street = kw.get("street")
        state = kw.get("state")
        country = kw.get("country")
        city = kw.get("city")
        email = kw.get("email")
        phone = kw.get("phone")
        gender = kw.get("gender")
        phone = kw.get("phone")
        experience_info = kw.get("experience_info")
        expected_salary = kw.get("expected_salary")
        job_position = kw.get("job_position")
        if kw:
            print(kw)
            employee = request.env["create.employees"].sudo().create(kw)
        return request.redirect("/create_employees")


    @http.route("/employee_details", type="http", website=True, auth="user", csrf=False)
    def employee_details(self, **kw):
        job_position = request.env["hr.job"].sudo().search([])
        values = {"job_position": job_position, 'submit': False}
        if kw:
            jp, filtered_employee = False, False
            if kw.get('job_position'):
                jp = int(kw.get('job_position'))
                filtered_employee = request.env["create.employees"].sudo().search([('job_position', '=', jp)])
            values.update({'submit': True, 'filtered_employee': filtered_employee,'jp':jp})
        return request.render("create_employees.employees_details_template", values)

    # @http.route("/filter_employee_details",type="http", website=True, auth="user", csrf=False)
    # def filter_employee_details(self,**kw):
    #
    #     if jp:
    #         return request.render("create_employees.employee_details_template", {"filtered_employee": filtered_employee})
    #     else:
    #         return request.redirect("/employee_details")
