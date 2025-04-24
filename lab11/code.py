import psycopg2


def get_connection():
    return psycopg2.connect("dbname=postgres user=postgres password=123 host=localhost")


def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS PhoneBook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100),
            last_name VARCHAR(100),
            phone_number VARCHAR(15),
            email VARCHAR(100)
        );
    """)
    conn.commit()
    cur.close()
    conn.close()


def search_by_pattern(pattern):
    if not pattern:
        print("Pattern is empty!")
        return

    conn = get_connection()
    cur = conn.cursor()
    query = """
        SELECT * FROM PhoneBook
        WHERE first_name ILIKE %s
           OR last_name ILIKE %s
           OR phone_number ILIKE %s;
    """
    params = (f"%{pattern}%", f"%{pattern}%", f"%{pattern}%")
    cur.execute(query, params)

    rows = cur.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("No records found.")

    cur.close()
    conn.close()


def insert_or_update_user(first_name, last_name, phone_number, email):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM PhoneBook WHERE first_name = %s AND last_name = %s", (first_name, last_name))
    record = cur.fetchone()

    if record:
        cur.execute("""
            UPDATE PhoneBook 
            SET phone_number = %s, email = %s 
            WHERE first_name = %s AND last_name = %s
        """, (phone_number, email, first_name, last_name))
    else:
        cur.execute("""
            INSERT INTO PhoneBook (first_name, last_name, phone_number, email) 
            VALUES (%s, %s, %s, %s)
        """, (first_name, last_name, phone_number, email))

    conn.commit()
    cur.close()
    conn.close()


def insert_many_users():
    conn = get_connection()
    cur = conn.cursor()
    invalids = ''

    while True:
        print("\nEnter user details:")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        phone_number = input("Phone Number: ")
        email = input("Email: ")

        insert_or_update_user(first_name, last_name, phone_number, email)

        more = input("Do you want to add another user? (y/n): ")
        if more.lower() != 'y':
            break

    conn.commit()
    cur.close()
    conn.close()


def delete_by_user_or_phone(username=None, phone_number=None):
    conn = get_connection()
    cur = conn.cursor()

    if username:
        cur.execute("DELETE FROM PhoneBook WHERE first_name = %s;", (username,))
    if phone_number:
        cur.execute("DELETE FROM PhoneBook WHERE phone_number = %s;", (phone_number,))

    conn.commit()
    cur.close()
    conn.close()


def get_paginated_data(limit_val, offset_val):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE OR REPLACE FUNCTION get_paginated_data(limit_val INT, offset_val INT)
        RETURNS TABLE(id INT, first_name VARCHAR(100), last_name VARCHAR(100), phone_number VARCHAR(15), email VARCHAR(100))
        AS $$
        BEGIN
            RETURN QUERY
            SELECT * FROM PhoneBook
            ORDER BY id
            LIMIT limit_val OFFSET offset_val;
        END;
        $$ LANGUAGE plpgsql;
    """)
    conn.commit()
    cur.close()
    conn.close()


def main():
    create_table()

    p = input("Enter pattern for search: ")
    search_by_pattern(p)

    insert_many_users()

    limit = int(input("Enter limit for pagination: "))
    offset = int(input("Enter offset for pagination: "))
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_paginated_data(%s, %s);", (limit, offset))
    results = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()

    for row in results:
        print(row)

    f_name_to_delete = input("Enter first name or phone number to delete: ")
    delete_by_user_or_phone(username=f_name_to_delete)


if __name__ == "__main__":
    main()
