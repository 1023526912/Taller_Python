from pathlib import Path

PROCESSED = Path(__file__).parent / "Data" / "processed"


def validar_premerge(clientes, ventas):
    """Revisa que el merge se pueda hacer. Devuelve True si todo está bien, False si no.

    Revisar:
    - Que exista la columna "id_cliente" en los dos dataframes.
    - Que "id_cliente" no esté repetido en clientes.
    - Que "id_cliente" tenga el mismo tipo en los dos dataframes.
    - Cuántas ventas no tienen cliente asociado (esto solo se informa, no falla).
    """
    for nombre, tabla in [("clientes", clientes), ("ventas", ventas)]:
        if "id_cliente" not in tabla.columns:
            print("Falta id_cliente en", nombre)
            return False
        if tabla["id_cliente"].isna().any():
            print("Hay identificadores nulos en", nombre)
            return False
    if clientes["id_cliente"].duplicated().any():
        print("Hay id_cliente repetidos en clientes")
        return False
    if clientes["id_cliente"].dtype != ventas["id_cliente"].dtype:
        print("Los tipos de id_cliente no coinciden")
        return False
    sin_cliente = (~ventas["id_cliente"].isin(clientes["id_cliente"])).sum()
    print("Ventas sin cliente asociado:", sin_cliente)
    print("Validación correcta: columnas, identificadores únicos y tipos compatibles.")
    return True


def unir(clientes, ventas):
    """Une ventas con clientes usando "id_cliente" y guarda el resultado en Data/processed/merge.csv.

    Pistas:
    - Usar pd.merge(...) o ventas.merge(...).
    - Usar how="left" para no perder ventas.
    - Usar validate="m:1" para confirmar que cada venta tiene un solo cliente.
    - Guardar con df.to_csv(...) en PROCESSED / "merge.csv".
    """
    if not validar_premerge(clientes, ventas):
        return None
    df = ventas.merge(clientes, on="id_cliente", how="left", validate="m:1")
    PROCESSED.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED / "merge.csv", index=False)
    print("Dimensiones del merge:", df.shape)
    print(df.head().to_string(index=False))
    print("Guardado en Data/processed/merge.csv")
    return df
