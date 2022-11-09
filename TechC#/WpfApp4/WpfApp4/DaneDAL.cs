using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Data;

namespace WpfApp4
{
    class DaneDAL
    {
        private SqlConnection sqlConnection = null;
        private String findAll = "SELECT * FROM t_dane";

        public void OpenConnection(String connectionString)
        {
            sqlConnection = new SqlConnection(connectionString);
            sqlConnection.Open();
            String serverVersion = sqlConnection.ServerVersion;
        }
        public void CloseConnection()
        {
            sqlConnection.Close();
        }

        public List<RowData> GetAllDane()
        {
            List<RowData> dataRows = new List<RowData>();

            using (SqlCommand command = new SqlCommand(findAll, sqlConnection))
            {
                SqlDataReader dataReader = command.ExecuteReader();
                while (dataReader.Read())
                {
                    RowData row = new RowData(
                                (dataReader["id"] != null) ? (long)dataReader["id"] : -1L,
                                (dataReader["nr"] != null) ? (String)dataReader["nr"] : "",
                                (dataReader["tytul"] != null) ? (String)dataReader["tytul"] : "",
                                (dataReader["kwota"] != null) ? (Decimal)dataReader["kwota"] : 0.00m,
                                (dataReader["opis"] != null) ? (String)dataReader["opis"] : "",
                                (!dataReader.IsDBNull(dataReader.GetOrdinal("obraz"))) ? (Byte[])dataReader["obraz"] : null);
                    dataRows.Add(row);
                }
                dataReader.Close();
            }
            return dataRows;
        }
    }
}
