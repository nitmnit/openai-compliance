# save this as app.py
from flask import Flask, request, jsonify

from utils import ComplianceUtil

app = Flask(__name__)

@app.route("/v1/compliance-issues/", methods=["POST"])
def find_compliance_issues():
    """
    Payload: 
    {
        "web_pae": "<test url>"
    }
    Returns:
    {
        "content": "<ChatGPT Feedback>"
    }
    """
    data = request.get_json()
    app.logger.info(f"request: /v1/compliance-issues/, payload: {data}")
    if "web_page" not in data:
        return jsonify({'error': 'web_page is required'}), 400
    compliance_url = "https://stripe.com/docs/treasury/marketing-treasury"
    pitch_url = data.get("web_page")
    results = {"content": ComplianceUtil.find_compliance(compliance_url, pitch_url)}
    app.logger.info(f"response: /v1/compliance-issues/, payload: {data}, response: {results}")
    return jsonify(results), 200
