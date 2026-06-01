import os
from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY,MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)

class AnimeRecommendationPipeline:
    def __init__(self,persist_dir="chroma_db", embedding=None):
        try:
            logger.info("Initializing Recommendation Pipeline")

            # Get the path to the CSV file relative to this file's location
            current_dir = os.path.dirname(os.path.abspath(__file__))
            csv_path = os.path.join(current_dir, "..", "data", "anime_with_synopsis.csv")

            # Check if vector store exists and has data
            vector_store_exists = os.path.exists(persist_dir) and len(os.listdir(persist_dir)) > 0
            
            vector_builder = VectorStoreBuilder(csv_path=csv_path, persist_dir=persist_dir, embedding=embedding)

            # Build vector store if it doesn't exist
            if not vector_store_exists:
                logger.info(f"Vector store not found. Building from {csv_path}...")
                vector_builder.build_and_save_vectorstore()
                logger.info("Vector store built successfully")

            retriever = vector_builder.load_vector_store().as_retriever()

            self.recommender = AnimeRecommender(retriever,GROQ_API_KEY,MODEL_NAME)

            logger.info("Pipeline initialized successfully...")

        except Exception as e:
            logger.error(f"Failed to intialize pipeline {str(e)}")
            raise CustomException("Error during pipeline intialization" , e)
        
    def recommend(self,query:str) -> str:
        try:
            logger.info(f"Recived a query {query}")

            recommendation = self.recommender.get_recommendation(query)

            logger.info("Recommendation generated sucesfulyy...")
            return recommendation
        except Exception as e:
            logger.error(f"Failed to get recommendation {str(e)}")
            raise CustomException("Error during getting recommendation" , e)
        


        