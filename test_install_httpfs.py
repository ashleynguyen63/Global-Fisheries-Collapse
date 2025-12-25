import traceback
try:
    import ibis
    import ibis.duckdb
    con = ibis.duckdb.connect()
    print('Connected to duckdb via ibis, running INSTALL httpfs;')
    con.execute("INSTALL httpfs;")
    print('INSTALL succeeded, now LOAD httpfs;')
    con.execute("LOAD httpfs;")
    print('LOAD succeeded')
except Exception as e:
    print('ERROR:')
    traceback.print_exc()
    raise
