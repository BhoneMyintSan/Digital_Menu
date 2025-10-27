# Digital Menu System

A desktop application for managing and viewing digital restaurant menus with multilingual support (Thai and English). The application connects to an Oracle database and provides an intuitive GUI for browsing menus, items, descriptions, and images.

## Features

- **Menu Browsing**: View all available menus organized by shop
- **Multilingual Support**: Display menu items in both Thai and English
- **Image Gallery**: View item images fetched from remote URLs
- **Detailed Descriptions**: Read comprehensive descriptions of menu items
- **Database Integration**: Seamless connection to Oracle database
- **User-Friendly GUI**: Built with Tkinter for easy navigation

## Project Structure

```
Digital_Menu/
├── app.py                 # Main application GUI
├── db_connection.py       # Database connection configuration
├── fetch_menus.py         # Database query functions
├── test.py                # Oracle client version test
└── README.md              # Project documentation
```

## Prerequisites

- Python 3.x
- Oracle Database access
- Oracle Instant Client

## Dependencies

Install the required Python packages:

```bash
pip install cx_Oracle Pillow validators
```

### Required Libraries:
- `cx_Oracle` - Oracle Database connectivity
- `tkinter` - GUI framework (usually included with Python)
- `Pillow (PIL)` - Image processing and display
- `validators` - URL validation
- `requests` - HTTP requests for fetching images

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/BhoneMyintSan/Digital_Menu.git
   cd Digital_Menu
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure database connection**
   
   Edit `db_connection.py` with your Oracle database credentials:
   ```python
   conn = cx_Oracle.connect('username/password@//host:port/service_name')
   ```

4. **Verify Oracle Client installation**
   ```bash
   python test.py
   ```

## Usage

### Running the Application

```bash
python app.py
```

### How to Use

1. **Load Menus**: Click the "Load Menus" button to fetch all available menus from the database
2. **Select a Shop**: Click on any menu row to view items from that shop
3. **View Item Details**: 
   - Select an item to view its full description
   - Item images will be displayed automatically (if available)
4. **Browse Items**: Navigate through different items using the translations window

## Database Schema

The application expects the following Oracle database tables:

### Tables:
- **Shop**: Shop information
  - `Shop_ID`, `Shop_Name`
- **Menu**: Menu listings
  - `Menu_ID`, `Menu_Name`, `Shop_ID`
- **Menu_Item**: Individual menu items
  - `Item_ID`, `Menu_ID`, `Thai_Name`
- **Translation**: English translations and descriptions
  - `Item_ID`, `English_Name`, `Description`
- **Image**: Item images
  - `Item_ID`, `Image_URL`

## Features Breakdown

### Main Window (app.py)
- Displays all menus with their associated shops
- Provides a "Load Menus" button to refresh data
- Allows selection to view detailed translations

### Translations Window
- Shows menu items in both Thai and English
- Displays item descriptions in a text box
- Shows item images (250x250 pixels)
- Handles image loading errors gracefully

### Database Functions (fetch_menus.py)
- `fetch_menus()`: Retrieves all menus with shop information
- `fetch_translations(shop_name)`: Gets translations for a specific shop
- `fetch_image_url(item_id)`: Fetches and validates image URLs

## Error Handling

- Database connection errors are caught and displayed via message boxes
- Invalid image URLs are detected and handled gracefully
- Missing data is handled with appropriate default messages

## Configuration

### Database Connection
Update the connection string in `db_connection.py`:
```python
conn = cx_Oracle.connect('DBMS128/matsushima@//tetraserver.thddns.net:4421/orcl')
```

### Image Display
Images are automatically resized to 250x250 pixels using `Image.LANCZOS` for best quality.

## Development

### Testing Database Connection
```bash
python test.py
```

This will display the Oracle Client version if properly configured.

### Modifying Queries
All SQL queries are located in `fetch_menus.py` and can be customized based on your database schema.

## Troubleshooting

### Common Issues:

1. **Oracle Client not found**
   - Install Oracle Instant Client
   - Add Oracle Client to system PATH

2. **Database connection failed**
   - Verify credentials in `db_connection.py`
   - Check network connectivity to database server
   - Ensure Oracle listener is running

3. **Images not loading**
   - Check internet connectivity
   - Verify image URLs in database are valid
   - Check firewall settings

4. **Module import errors**
   - Ensure all dependencies are installed: `pip install -r requirements.txt`

## Future Enhancements

- [ ] Add search functionality
- [ ] Implement menu editing capabilities
- [ ] Add user authentication
- [ ] Export menu data to PDF
- [ ] Support for more languages
- [ ] Category filtering
- [ ] Price management
- [ ] Order placement system

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is available for educational and commercial use.

## Author

**Bhone Myint San**
- GitHub: [@BhoneMyintSan](https://github.com/BhoneMyintSan)

## Contact

For questions or support, please open an issue on GitHub.

---

**Note**: Make sure to keep your database credentials secure and never commit them to public repositories. Consider using environment variables for sensitive configuration.
