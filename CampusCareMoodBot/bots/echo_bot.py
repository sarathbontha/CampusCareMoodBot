import os

from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


class EchoBot(ActivityHandler):

    def __init__(self):
        endpoint = os.environ.get("LANGUAGE_ENDPOINT", "")
        key = os.environ.get("LANGUAGE_KEY", "")

        if endpoint and key:
            credential = AzureKeyCredential(key)
            self.client = TextAnalyticsClient(
                endpoint=endpoint,
                credential=credential,
            )
        else:
            self.client = None

    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity(
                    "Welcome to CampusCare Mood Assistant!\n"
                    "Type 'help' to see my capabilities."
                )

    async def on_message_activity(self, turn_context: TurnContext):

        user_message = turn_context.activity.text.strip()
        message = user_message.lower()

        if message in ["hi", "hello", "hey"]:

            response = (
                "Hello! Welcome to CampusCare Mood Assistant."
            )

        elif message == "help":

            response = (
                "I can help you with:\n\n"
                "• hello\n"
                "• analyze\n"
                "• about\n"
                "• privacy\n"
                "• bye\n\n"
                "Type 'analyze' and then send any feedback sentence."
            )

        elif message == "about":

            response = (
                "I am a traditional chatbot integrated with Azure AI "
                "Language Sentiment Analysis."
            )

        elif message == "privacy":

            response = (
                "Please avoid entering passwords, account numbers, or "
                "other sensitive personal information."
            )

        elif message in ["bye", "exit"]:

            response = (
                "Goodbye! Thank you for using CampusCare Mood Assistant."
            )

        elif message == "analyze":

            response = (
                "Please type any sentence describing your campus experience."
            )

        else:

            if self.client is None:

                response = (
                    "Azure AI service is not configured."
                )

            else:

                try:

                    documents = [user_message]

                    result = self.client.analyze_sentiment(documents)[0]

                    sentiment = result.sentiment.title()

                    positive = round(
                        result.confidence_scores.positive,
                        2,
                    )

                    neutral = round(
                        result.confidence_scores.neutral,
                        2,
                    )

                    negative = round(
                        result.confidence_scores.negative,
                        2,
                    )

                    if sentiment == "Positive":

                        advice = (
                            "Thank you for sharing your positive feedback."
                        )

                    elif sentiment == "Negative":

                        advice = (
                            "I am sorry you had a negative experience."
                        )

                    elif sentiment == "Mixed":

                        advice = (
                            "Your feedback contains both positive and negative opinions."
                        )

                    else:

                        advice = (
                            "Thank you for sharing your feedback."
                        )

                    response = (
                        f"Overall Sentiment: {sentiment}\n\n"
                        f"Positive Score: {positive}\n"
                        f"Neutral Score: {neutral}\n"
                        f"Negative Score: {negative}\n\n"
                        f"{advice}"
                    )

                except Exception as ex:

                    response = (
                        "Unable to connect to Azure AI Language Service.\n\n"
                        f"Error: {str(ex)}"
                    )

        await turn_context.send_activity(response)