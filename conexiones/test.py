from adaptadores import conexion_db

def probar_conexion():
    conn = conexion_db()
    if conn:
        print("✅ Conexión exitosa a la base de datos.")
        conn.close()
    else:
        print("❌ No se pudo conectar a la base de datos.")

probar_conexion()