# save this as app.py
from flask import Flask, request, jsonify
from marshmallow import ValidationError
from schema import ComplianceIssuesSchema
import config

from utils import ComplianceUtil

app = Flask(__name__)

@app.route("/v1/compliance-issues/", methods=["POST"])
def find_compliance_issues():
    """
    Payload: 
    {
        "web_page": "<test url>"
    }
    Returns:
    {
        "content": "<ChatGPT Feedback>"
    }
    """
    json_data = request.get_json()
    app.logger.info(f"request: /v1/compliance-issues/, payload: {json_data}")
    try:
        data = ComplianceIssuesSchema().load(json_data)
    except ValidationError as err:
        return err.messages, 400
    results = {"content": ComplianceUtil.find_compliance(config.COMPLIANCE_URL, data.get("web_page"))}
    app.logger.info(f"response: /v1/compliance-issues/, payload: {data}, response: {results}")
    return jsonify(results), 200
