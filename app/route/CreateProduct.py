from pathlib import Path
from .IDatabase import DatabaseConnection

class ICreateProduct:
    def __init__(self):
        self.conn = DatabaseConnection()
        self.cursor = self.conn.cursor

    def image_to_binary(self, image_path):
        """Convert the image to binary data."""
        with open(image_path, 'rb') as file:
            return file.read()

    def convert_type(self, option):
        if option == "option0":
            product_type = "none"
        elif option == "option1":
            product_type = "snack"
        elif option == "option2":
            product_type = "water"
        elif option == "option3":
            product_type = "cleaning"
        elif option == "option4":
            product_type = "skincare"
        elif option == "option5":
            product_type = "meds"
        # elif option == "option6":
        #     product_type = "pendants"
        return product_type

    async def create_product(self, name, info, file_pic, stock_quantity, product_type, price, code):
        """Insert a new product with an image into the database."""
        # Construct the absolute path to the img folder
        image_path = Path(__file__).resolve().parent.parent / 'img' / f'{file_pic}'
        image_name = file_pic

        # # Convert the image to binary
        image_data = self.image_to_binary(image_path)
        # image_data = self.image_to_binary(image_name.split(".")[0])

        product_type = self.convert_type(product_type)

        # Insert the product into the database
        self.cursor.execute(
            'INSERT INTO product(name, information, file_pic, pic, stock_quantity, type, price, code) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
            (name, info, image_name, image_data, stock_quantity, product_type, price, code)
        )

        # Commit the transaction
        self.conn.commit()

        print("Product with image inserted successfully.")

    def close_connection(self):
        """Close the database connection."""
        self.conn.close()
