# Import PyMySQL as Django database backend
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass
