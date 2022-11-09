using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace WpfApp4
{
    /// <summary>
    /// Logika interakcji dla klasy MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        String connectionString = 
        @"Data Source = 155.158.112.31;Initial Catalog=tomcat;User id=tomcatUser;Password=tomcat;";

        private ObservableCollection<RowData> RowDataList { get; set; }

        public MainWindow()
        {
            RowDataList = new ObservableCollection<RowData>();
            InitializeComponent();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            DaneDAL daneDAL = new DaneDAL();
            daneDAL.OpenConnection(connectionString);
            List<RowData> dataRows = daneDAL.GetAllDane();
            daneDAL.CloseConnection();

            RowDataList.Clear();
            foreach (RowData row in dataRows)
            {
                RowDataList.Add(row);
            }
        }
    }
}
