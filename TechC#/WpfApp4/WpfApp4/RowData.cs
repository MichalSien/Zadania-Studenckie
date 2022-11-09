using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WpfApp4
{
    class RowData
    {
        public long Id { get; set; }
        public String Nr { get; set; }
        public String Tytul { get; set; }
        public Decimal Kwota { get; set; }
        public String Opis { get; set; }
        public Byte[] Obraz { get; set; }

        public RowData(long id, String nr, String tytul, Decimal kwota, String opis, Byte[] obraz)
        {
            Id = id;
            Nr = nr;
            Tytul = tytul;
            Kwota = kwota;
            Opis = opis;
            Obraz = obraz;
        }
    }
}
