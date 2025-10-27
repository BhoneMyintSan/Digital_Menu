import validators# Updated fetch_menus.py
import cx_Oracle
from db_connection import conn

def fetch_menus():
    cursor = conn.cursor()
    query = """
    SELECT m.Menu_ID, m.Menu_Name, s.Shop_Name
    FROM Menu m
    JOIN Shop s ON m.Shop_ID = s.Shop_ID
    ORDER BY m.Menu_ID
    """
    cursor.execute(query)
    menus = cursor.fetchall()
    cursor.close()
    return menus

def fetch_translations(shop_name):
    cursor = conn.cursor()
    query = """
    SELECT s.Shop_Name, mi.Item_ID, mi.Thai_Name, t.English_Name, t.Description
    FROM Shop s
    JOIN Menu m ON s.Shop_ID = m.Shop_ID
    JOIN Menu_Item mi ON m.Menu_ID = mi.Menu_ID
    JOIN Translation t ON mi.Item_ID = t.Item_ID
    WHERE s.Shop_Name = :shop_name
    ORDER BY mi.Item_ID
    """
    cursor.execute(query, {'shop_name': shop_name})
    translations = cursor.fetchall()
    cursor.close()
    return translations

def fetch_image_url(item_id):
    cursor = conn.cursor()
    query = "SELECT Image_URL FROM Image WHERE Item_ID = :item_id"
    cursor.execute(query, {'item_id': item_id})
    image = cursor.fetchone()
    cursor.close()
    
    if image and image[0]:
        url = image[0].strip()
        if validators.url(url):  # Check if the URL is valid
            return url
    return "No valid image available"
