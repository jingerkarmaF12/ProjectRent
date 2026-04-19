from dotenv import load_dotenv
from pathlib import Path
import os

dotenv_path = Path(__file__).resolve().parent / ".env"
if not dotenv_path.exists():
    raise FileNotFoundError(f".env file not found at {dotenv_path}")

load_dotenv(dotenv_path)

from database_management import Base, engine
# Import all models to ensure they are registered with Base.metadata
from Users import Users
from listings import Listings
from property_details import PropertyDetails
from listing_images import ListingImages
from applications import Applications
from favorites import Favorites
from whatsapp_groups import WhatsAppGroups
from group_listings import GroupListings
from messages import Messages
from reports import Reports

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully.")
