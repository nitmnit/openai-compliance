from marshmallow import Schema, fields


class ComplianceIssuesSchema(Schema):
    web_page = fields.URL(required=True)


class ComplianceIssuesV2Schema(Schema):
    web_page = fields.URL(required=True)
    guidelines_url = fields.URL(required=True)
