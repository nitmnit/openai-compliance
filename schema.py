from marshmallow import Schema, fields


class ComplianceIssuesSchema(Schema):
    web_page = fields.URL(required=True)
