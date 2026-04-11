import asyncio
import os

from agent_framework.azure import AzureOpenAIChatClient


def get_weather(city: str) -> str:
    """Learning-only sample tool."""
    weather_map = {
        "tokyo": "Tokyo is sunny.",
        "osaka": "Osaka is cloudy.",
        "sapporo": "Sapporo is snowy.",
    }
    return weather_map.get(city.lower(), f"{city} weather is unavailable.")


async def main() -> None:
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

    if not endpoint or not api_key or not deployment_name:
        raise ValueError(
            "Set AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_KEY, and "
            "AZURE_OPENAI_DEPLOYMENT before running."
        )

    async with (
        AzureOpenAIChatClient(
            endpoint=endpoint,
            api_key=api_key,
            deployment_name=deployment_name,
        ).create_agent(
            instructions=(
                "You are a helpful study assistant. "
                "Answer briefly. "
                "Use the weather tool only when the question needs current weather."
            ),
            tools=[get_weather],
        ) as agent,
    ):
        print("=== First turn ===")
        first = await agent.run("What is a Python dictionary?")
        print(first)

        print("\n=== Second turn ===")
        second = await agent.run("Tell me the weather in Tokyo too.")
        print(second)


if __name__ == "__main__":
    asyncio.run(main())
