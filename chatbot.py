def get_reply(message):

    message = message.lower()

    if "sip" in message:
        return "SIP helps you invest monthly."

    elif "mutual" in message:
        return "We provide Equity, Hybrid and Debt Mutual Funds."

    elif "insurance" in message:
        return "We provide Health, Life and Term Insurance."

    elif "hello" in message or "hi" in message:
        return """Welcome to Polaris Financial Services.

1️ Mutual Funds / SIP
2️ Health Insurance
3️ Term Insurance
4️ Tax Saving Investments
5️ Not interested right now
"""

    return "Please choose a valid option."
