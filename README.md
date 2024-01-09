# openai-compliance
Find non-compliant web pages using AI.

## Version 1
- Use beautifulsoup to fetch the web pages and pass content to opanai APIs as instructions to answer for given page content, find all the non-compliant results.
- Sample Request
```sh
curl --location 'http://localhost:5000/v1/compliance-issues/' \
--header 'Content-Type: application/json' \
--data '{
    "web_page": "https://www.joinguava.com/"
}'
```
- Sample Response
```json
{
  "content": "There are a few sentences in the marketing idea that don't comply with the compliance guidelines:\n\n1. \"Get The Banking You Deserve\" - This sentence implies that Guava is a banking platform, which is a term to avoid. Instead, it should be rephrased to something like \"Get the Financial Services You Deserve\" or \"Get the Money Management You Deserve.\"\n\n2. \"A digital banking platform with free financial tools for your small business\" - Again, this sentence implies that Guava is a banking platform. It should be rephrased to something like \"A digital platform with free financial tools for your small business\" or \"A digital financial service platform with free tools for your small business.\"\n\n3. \"Create your business checking account for free in minutes with instant access to a virtual debit card.\" - This sentence implies that Guava offers a banking product. It should be rephrased to something like \"Create your business money management account for free in minutes with instant access to a virtual debit card.\"\n\n4. \"Pay bills, transfer funds, check your balance, and more -- anytime, anywhere from our app.\" - This sentence implies that Guava offers banking services. It should be rephrased to something like \"Manage your funds, track your transactions, and more -- anytime, anywhere from our app.\"\n\n5. \"Connect your Guava virtual card to Apple Wallet or Google Pay for secure, easy, and quick contactless payments.\" - This sentence implies that Guava offers a banking product. It should be rephrased to something like \"Connect your Guava virtual card to Apple Wallet or Google Pay for secure, easy, and quick contactless transactions.\"\n\n6. \"Export your transaction activity into a CSV file for easy uploading to reconciliation tools.\" - This sentence implies that Guava offers banking services. It should be rephrased to something like \"Export your transaction activity into a CSV file for easy reconciliation.\"\n\n7. \"We're not just a banking platform. We're a trusted network of peers and experts here to help you thrive.\" - This sentence implies that Guava is a banking platform. It should be rephrased to something like \"We're not just a financial platform. We're a trusted network of peers and experts here to help you thrive.\"\n\n8. \"Nationwide ATMs\" - This sentence implies that Guava offers banking services. It should be rephrased to something like \"Access to nationwide ATMs.\"\n\n9. \"No Hidden Fees\" - This sentence implies that Guava offers banking services. It should be rephrased to something like \"Transparent Pricing\" or \"No Surprise Fees.\"\n\n10. \"Smart Spend\" - This sentence implies that Guava offers banking services. It should be rephrased to something like \"Smart Money Management\" or \"Intelligent Spending.\"\n\n11. \"Guava isn\u2019t just a banking platform, it\u2019s a community.\" - This sentence implies that Guava is a banking platform. It should be rephrased to something like \"Guava isn't just a financial platform, it's a community.\"\n\n12. \"Banking services provided by Piermont Bank, Member FDIC.\" - This sentence implies that Guava offers banking services. It should be rephrased to something like \"Financial services provided by Piermont Bank, Member FDIC.\"\n\nPlease note that these are just suggestions for rephrasing the sentences to comply with the guidelines. It's important to review the entire marketing idea and make sure all the content aligns with the compliance guidelines."
}
```
- Readable content output
```text
There are a few sentences in the marketing idea that don't comply with the compliance guidelines:

1. "Get The Banking You Deserve" - This sentence implies that Guava is a banking platform, which is a term to avoid. Instead, it should be rephrased to something like "Get the Financial Services You Deserve" or "Get the Money Management You Deserve."

2. "A digital banking platform with free financial tools for your small business" - Again, this sentence implies that Guava is a banking platform. It should be rephrased to something like "A digital platform with free financial tools for your small business" or "A digital financial service platform with free tools for your small business."

3. "Create your business checking account for free in minutes with instant access to a virtual debit card." - This sentence implies that Guava offers a banking product. It should be rephrased to something like "Create your business money management account for free in minutes with instant access to a virtual debit card."

4. "Pay bills, transfer funds, check your balance, and more -- anytime, anywhere from our app." - This sentence implies that Guava offers banking services. It should be rephrased to something like "Manage your funds, track your transactions, and more -- anytime, anywhere from our app."

5. "Connect your Guava virtual card to Apple Wallet or Google Pay for secure, easy, and quick contactless payments." - This sentence implies that Guava offers a banking product. It should be rephrased to something like "Connect your Guava virtual card to Apple Wallet or Google Pay for secure, easy, and quick contactless transactions."

6. "Export your transaction activity into a CSV file for easy uploading to reconciliation tools." - This sentence implies that Guava offers banking services. It should be rephrased to something like "Export your transaction activity into a CSV file for easy reconciliation."

7. "We're not just a banking platform. We're a trusted network of peers and experts here to help you thrive." - This sentence implies that Guava is a banking platform. It should be rephrased to something like "We're not just a financial platform. We're a trusted network of peers and experts here to help you thrive."

8. "Nationwide ATMs" - This sentence implies that Guava offers banking services. It should be rephrased to something like "Access to nationwide ATMs."

9. "No Hidden Fees" - This sentence implies that Guava offers banking services. It should be rephrased to something like "Transparent Pricing" or "No Surprise Fees."

10. "Smart Spend" - This sentence implies that Guava offers banking services. It should be rephrased to something like "Smart Money Management" or "Intelligent Spending."

11. "Guava isn’t just a banking platform, it’s a community." - This sentence implies that Guava is a banking platform. It should be rephrased to something like "Guava isn't just a financial platform, it's a community."

12. "Banking services provided by Piermont Bank, Member FDIC." - This sentence implies that Guava offers banking services. It should be rephrased to something like "Financial services provided by Piermont Bank, Member FDIC."

Please note that these are just suggestions for rephrasing the sentences to comply with the guidelines. It's important to review the entire marketing idea and make sure all the content aligns with the compliance guidelines.
```

## Installation
- Go to your github codespaces settings to add OpenAI API key as secrets: https://github.com/settings/codespaces
- Create `New Secret` by name `OPENAI_API_KEY` and set the value. In repository, select this repository.
- On github repository page and change branch to `version1`
- Go to `Code` -> `Codespaces` -> `Create codespace on version1`
- In codespace, go to `Run and Debug` (Ctrl+Shift+d)
- Run `Python: Flask`
- To test API, in terminal within codespaces (Ctrl+`), make a curl request
```sh
curl --location 'http://localhost:5000/v1/compliance-issues/' \
--header 'Content-Type: application/json' \
--data '{
    "web_page": "https://www.joinguava.com/"
}'
```
- Go to `Testing` in left panel to run all the tests.
