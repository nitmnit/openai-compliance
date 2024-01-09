# openai-compliance
Find non-compliant web pages using AI.

## Version 2
- Use beautifulsoup to fetch the web pages and pass content to opanai APIs as instructions to answer for given page content, find all the non-compliant results.
- Sample Request
```sh
curl --location 'http://localhost:5000/v1/compliance-issues/' \
--header 'Content-Type: application/json' \
--data '{
    "web_page": "https://www.joinguava.com/",
    "guidelines_url": "https://stripe.com/docs/treasury/marketing-treasury#recommended-terms"
}'
```
- Sample Response
```json
{
  "content": "The marketing idea contains several sentences that do not follow the compliance guidelines. Here are the sentences that need to be revised:\n\n1. \"Get The Banking You Deserve\" - This sentence implies that Guava offers banking services, which may draw scrutiny from regulators.\n\n2. \"A digital banking platform with free financial tools for your small business\" - Again, this sentence suggests that Guava provides banking services, which is not compliant with the guidelines.\n\n3. \"Create your business checking account for free in minutes with instant access to a virtual debit card\" - This sentence uses the term \"checking account,\" which should be avoided in marketing programs.\n\n4. \"Pay bills, transfer funds, check your balance, and more -- anytime, anywhere from our app\" - The term \"transfer funds\" implies banking services, which is not compliant.\n\n5. \"Easily connect your business checking account to Venmo, Etsy, Shopify, Stripe, and more\" - The term \"business checking account\" should be avoided.\n\n6. \"Connect your Guava virtual card to Apple Wallet or Google Pay for secure, easy, and quick contactless payments\" - The term \"virtual card\" should be replaced with a compliant term.\n\n7. \"Export your transaction activity into a CSV file for easy uploading to reconciliation tools\" - The term \"transaction activity\" should be revised to comply with the guidelines.\n\n8. \"We're not just a banking platform\" - This sentence contradicts the compliance guidelines and should be revised.\n\n9. \"Join other Guava members and feel seen, supported, and celebrated on your entrepreneurship journey\" - The term \"join\" implies membership in a banking platform, which is not compliant.\n\n10. \"Nationwide ATMs\" - This sentence suggests that Guava offers ATM services, which is not compliant.\n\n11. \"No minimum balance is required, ever\" - The term \"minimum balance\" should be avoided.\n\n12. \"Make smarter spending decisions and maximize your spending potential\" - The term \"spending potential\" should be revised to comply with the guidelines.\n\n13. \"The Guava Mastercard\u00ae Debit Card is issued by Piermont Bank, Member FDIC\" - This sentence implies that Guava offers a Mastercard debit card, which is not compliant.\n\nThese sentences should be revised to comply with the marketing compliance guidelines."
}
```
- Readable content output
```text
The marketing idea contains several sentences that do not follow the compliance guidelines. Here are the sentences that need to be revised:

1. "Get The Banking You Deserve" - This sentence implies that Guava offers banking services, which may draw scrutiny from regulators.

2. "A digital banking platform with free financial tools for your small business" - Again, this sentence suggests that Guava provides banking services, which is not compliant with the guidelines.

3. "Create your business checking account for free in minutes with instant access to a virtual debit card" - This sentence uses the term "checking account," which should be avoided in marketing programs.

4. "Pay bills, transfer funds, check your balance, and more -- anytime, anywhere from our app" - The term "transfer funds" implies banking services, which is not compliant.

5. "Easily connect your business checking account to Venmo, Etsy, Shopify, Stripe, and more" - The term "business checking account" should be avoided.

6. "Connect your Guava virtual card to Apple Wallet or Google Pay for secure, easy, and quick contactless payments" - The term "virtual card" should be replaced with a compliant term.

7. "Export your transaction activity into a CSV file for easy uploading to reconciliation tools" - The term "transaction activity" should be revised to comply with the guidelines.

8. "We're not just a banking platform" - This sentence contradicts the compliance guidelines and should be revised.

9. "Join other Guava members and feel seen, supported, and celebrated on your entrepreneurship journey" - The term "join" implies membership in a banking platform, which is not compliant.

10. "Nationwide ATMs" - This sentence suggests that Guava offers ATM services, which is not compliant.

11. "No minimum balance is required, ever" - The term "minimum balance" should be avoided.

12. "Make smarter spending decisions and maximize your spending potential" - The term "spending potential" should be revised to comply with the guidelines.

13. "The Guava Mastercard® Debit Card is issued by Piermont Bank, Member FDIC" - This sentence implies that Guava offers a Mastercard debit card, which is not compliant.

These sentences should be revised to comply with the marketing compliance guidelines.
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
    "web_page": "https://www.joinguava.com/",
    "guidelines_url": "https://stripe.com/docs/treasury/marketing-treasury#recommended-terms"
}'
```
- Go to `Testing` in left panel to run all the tests.
