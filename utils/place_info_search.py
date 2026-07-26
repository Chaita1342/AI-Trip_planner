# import os
# import json
# from langchain_tavily import TavilySearch
# from langchain_google_community import GooglePlacesTool, GooglePlacesAPIWrapper 

# class GooglePlaceSearchTool:
#     def __init__(self, api_key: str):
#         self.places_wrapper = GooglePlacesAPIWrapper(gplaces_api_key=api_key)
#         self.places_tool = GooglePlacesTool(api_wrapper=self.places_wrapper)
    
#     def google_search_attractions(self, place: str) -> dict:
#         """
#         Searches for attractions in the specified place using GooglePlaces API.
#         """
#         return self.places_tool.run(f"top attractive places in and around {place}")
    
#     def google_search_restaurants(self, place: str) -> dict:
#         """
#         Searches for available restaurants in the specified place using GooglePlaces API.
#         """
#         return self.places_tool.run(f"what are the top 10 restaurants and eateries in and around {place}?")
    
#     def google_search_activity(self, place: str) -> dict:
#         """
#         Searches for popular activities in the specified place using GooglePlaces API.
#         """
#         return self.places_tool.run(f"Activities in and around {place}")

#     def google_search_transportation(self, place: str) -> dict:
#         """
#         Searches for available modes of transportation in the specified place using GooglePlaces API.
#         """
#         return self.places_tool.run(f"What are the different modes of transportations available in {place}")

# class TavilyPlaceSearchTool:
#     def __init__(self):
#         pass

#     def tavily_search_attractions(self, place: str) -> dict:
#         """
#         Searches for attractions in the specified place using TavilySearch.
#         """
#         tavily_tool = TavilySearch(topic="general", include_answer="advanced")
#         result = tavily_tool.invoke({"query": f"top attractive places in and around {place}"})
#         if isinstance(result, dict) and result.get("answer"):
#             return result["answer"]
#         return result
    
#     def tavily_search_restaurants(self, place: str) -> dict:
#         """
#         Searches for available restaurants in the specified place using TavilySearch.
#         """
#         tavily_tool = TavilySearch(topic="general", include_answer="advanced")
#         result = tavily_tool.invoke({"query": f"what are the top 10 restaurants and eateries in and around {place}."})
#         if isinstance(result, dict) and result.get("answer"):
#             return result["answer"]
#         return result
    
#     def tavily_search_activity(self, place: str) -> dict:
#         """
#         Searches for popular activities in the specified place using TavilySearch.
#         """
#         tavily_tool = TavilySearch(topic="general", include_answer="advanced")
#         result = tavily_tool.invoke({"query": f"activities in and around {place}"})
#         if isinstance(result, dict) and result.get("answer"):
#             return result["answer"]
#         return result

#     def tavily_search_transportation(self, place: str) -> dict:
#         """
#         Searches for available modes of transportation in the specified place using TavilySearch.
#         """
#         tavily_tool = TavilySearch(topic="general", include_answer="advanced")
#         result = tavily_tool.invoke({"query": f"What are the different modes of transportations available in {place}"})
#         if isinstance(result, dict) and result.get("answer"):
#             return result["answer"]
#         return result
    






import os
import json
from dotenv import load_dotenv
from langchain_tavily import TavilySearch
from langchain_google_community import GooglePlacesTool, GooglePlacesAPIWrapper

# Load environment variables
load_dotenv()

class GooglePlaceSearchTool:
    def __init__(self, api_key: str):

        print("\n" + "=" * 70)
        print("DEBUGGING GOOGLE PLACES")
        print("=" * 70)
        print("Current Working Directory:", os.getcwd())
        print("Argument api_key:", repr(api_key))
        print("Environment GPLACES_API_KEY:", repr(os.getenv("GPLACES_API_KEY")))
        print("=" * 70 + "\n")

        # If api_key wasn't passed, use the environment variable
        if not api_key:
            api_key = os.getenv("GPLACES_API_KEY")

        if not api_key:
            raise ValueError(
                "GPLACES_API_KEY is empty. Check your .env file and load_dotenv()."
            )

        self.places_wrapper = GooglePlacesAPIWrapper(
            gplaces_api_key=api_key
        )

        self.places_tool = GooglePlacesTool(
            api_wrapper=self.places_wrapper
        )

    def google_search_attractions(self, place: str) -> dict:
        return self.places_tool.run(
            f"top attractive places in and around {place}"
        )

    def google_search_restaurants(self, place: str) -> dict:
        return self.places_tool.run(
            f"what are the top 10 restaurants and eateries in and around {place}?"
        )

    def google_search_activity(self, place: str) -> dict:
        return self.places_tool.run(
            f"Activities in and around {place}"
        )

    def google_search_transportation(self, place: str) -> dict:
        return self.places_tool.run(
            f"What are the different modes of transportations available in {place}"
        )


class TavilyPlaceSearchTool:
    def __init__(self):
        pass

    def tavily_search_attractions(self, place: str) -> dict:
        tavily_tool = TavilySearch(
            topic="general",
            include_answer="advanced"
        )

        result = tavily_tool.invoke(
            {"query": f"top attractive places in and around {place}"}
        )

        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]

        return result

    def tavily_search_restaurants(self, place: str) -> dict:
        tavily_tool = TavilySearch(
            topic="general",
            include_answer="advanced"
        )

        result = tavily_tool.invoke(
            {"query": f"what are the top 10 restaurants and eateries in and around {place}"}
        )

        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]

        return result

    def tavily_search_activity(self, place: str) -> dict:
        tavily_tool = TavilySearch(
            topic="general",
            include_answer="advanced"
        )

        result = tavily_tool.invoke(
            {"query": f"activities in and around {place}"}
        )

        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]

        return result

    def tavily_search_transportation(self, place: str) -> dict:
        tavily_tool = TavilySearch(
            topic="general",
            include_answer="advanced"
        )

        result = tavily_tool.invoke(
            {
                "query": f"What are the different modes of transportations available in {place}"
            }
        )

        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]

        return result