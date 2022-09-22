def get_DSN():
    driver, username, password, host, port, database = 'postgresql', 'postgres', 'postgres', 'localhost', '5432', 'homework3'
    DSN = f'{driver}://{username}:{password}@{host}:{port}/{database}'
    return DSN 