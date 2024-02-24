from base import Database

def create_table():
    print("test")
    '''Kategoriya'''
    category_table = f"""
        CREATE TABLE category(
            category_id SERIAL PRIMARY KEY,
            category_name VARCHAR(50),
            description VARCHAR(50));"""
    
    '''Firma'''
    firma_table = f"""
            CREATE TABLE firma(
            firma_id SERIAL PRIMARY KEY,
            firman_name VARCHAR(20),
            firma_addres VARCHAR(50),
            qr_number VARCHAR(20),
            date DATE );"""
    
    '''Mahsulot'''
    product_table = f"""
        CREATE TABLE product(
            product_id SERIAL PRIMARY KEY,
            product_name VARCHAR(20),
            product_number BIGINT,
            category_id INT REFERENCES category(category_id),
            product_date TIMESTAMP DEFAULT now(),
            firma_id INT REFERENCES firma(firma_id));"""
    
    '''Xaridor'''
    client_table = f"""
        CREATE TABLE client(
            client_id SERIAL PRIMARY KEY,
            client_name VARCHAR(25),
            client_number VARCHAR(20),
            client_addres VARCHAR(20),
            get_client TIMESTAMP DEFAULT now());"""
    
    '''Sotuvchi'''
    vendor_table = f"""
        CREATE TABLE vendor(
            vendor_id SERIAL PRIMARY KEY,
            vendor_name VARCHAR(20),
            vendor_number VARCHAR(15),
            vendor_addres VARCHAR(25));"""
    
    '''Dori'''
    drug_table = f"""
        CREATE TABLE drug(
            drug_id SERIAL PRIMARY KEY,
            drug_date TIMESTAMP NOT NULL,
            term_date TIMESTAMP NOT NULL,
            done VARCHAR(5),
            product_id INT REFERENCES product(product_id),
            client_id INT REFERENCES client(client_id),
            drog_number BIGINT DEFAULT 0);"""
    
    data_table = {
        "category_table": category_table,
        "firma_table": firma_table,
        "product_table": product_table,
        "client_table": client_table,
        "vendor_table": vendor_table,
        "drug_table": drug_table
    }
    for i in data_table:
        print(f"{i} {Database.connect(data_table[i], "create")}")

if __name__ == "__main__":
    create_table()