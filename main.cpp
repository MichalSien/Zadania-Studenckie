// PREORDER:
// wypisz siebie
// wypisz lewe poddrzewo
// wypisz prawe poddrzewo

// INORDER:
// wypisz lewe poddrzewo
// wypisz siebie
// wypisz prawe poddrzewo

// POSTORDER:
// wypisz lewe poddrzewo
// wypisz prawe poddrzewo
// wypisz siebie


/*
// Zadanie 1
// =========
struct Wezel
{
	Wezel *lewy;
	Wezel *prawy;
	int wartosc;
};


void wypisz(Wezel *korzen)
{
	if(korzen != nullptr)
	{ 
		wypisz(korzen->prawy);
		printf("%d\n", korzen->wartosc);
		wypisz(korzen->lewy);
	}
}


void wypisz2(Wezel *korzen)
{
	if(korzen != nullptr)
	{
		printf("%d\n", korzen->wartosc);
		// wypisz2(korzen->wartosc); - ZLE
		// printf("%d\n", korzen->lewy); - ZLE - wyswietli adres lewego poddrzewa
		wypisz2(korzen->prawy);
		wypisz2(korzen->lewy);
	}
}


void wypisz3(Wezel *wezel)
{
	if(korzen != nullptr)
	{
		wypisz(korzen->prawy);
		wypisz(korzen->lewy);
		printf("%d\n", korzen->wartosc);
	}
}


*/


/*
#include <iostream>
#include <sstream>

// Zadanie 3
// =========

std::string skompresuj(std::string ciag)
{
	int dlugosc = ciag.size();
	int i = 0;
	std::string wynik;
	while (i < dlugosc)
	{
		char znak = ciag[i];

		// liczymy ile razy pod rzad wystepuje znak
		int ile = 1;
		while(i + ile < dlugosc && ciag[i+ile] == znak)
			++ile;

		if (ile <= 2)
		{
			for(int k = 0; k < ile; ++k)
				wynik += znak;
		}
		else
		{
			wynik += znak;
			wynik += ';';

			// konwertujemy ile na lancuch
			std::ostringstream stream;
			stream << ile;
			wynik += stream.str();

			wynik += ';';
		}

		i += ile;
	}

	return wynik;
}


int main()
{
	std::cout << skompresuj("555555333352422279888") << std::endl;
	system("pause");
	return 0;
}
*/


/*
#include <iostream>


// 0 1 2 3 5 5 8 9 8
//               i, x = 2
//   j
void sortuj_przez_wstawianie(double *tablica, int rozmiar)
{
	for (int i = 1; i < rozmiar; ++i)
	{
		double x = tablica[i];
		int j = i-1;
		while(j >= 0 && tablica[j] > x)
		{ 
			tablica[j+1] = tablica[j];
			--j;
		}
		tablica[j+1] = x;
	}
}


int main()
{
	double t[] = { 4, 2, 7, 0, 1 };
	sortuj_przez_wstawianie(t, 5);
	for(int i = 0; i < 5; ++i)
		std::cout << t[i] << std::endl;
	system("pause");
	return 0;
}
*/


/*

#include <iostream>


// 4, 2, 7, 0, 1
// 0 2 7 4 1
// 0 1 7 4 2
// 0 1 2 4 7

void sortuj_przez_wybieranie(double *tablica, int rozmiar)
{
	for (int i = 0; i < rozmiar; ++i)
	{
		// szukamy najmniejszego elementu poczawszy od indeksu i
		int indeks_najmniejszego = i;
		for (int j = i + 1; j < rozmiar; ++j)
		{
			if(tablica[j] < tablica[indeks_najmniejszego])
				indeks_najmniejszego = j;
		}

		// zamieniamy element najmniejszy z elementem pod indeksem i
		std::swap(tablica[i], tablica[indeks_najmniejszego]);
	}
}


int main()
{
	double t[] = { 4, 2, 7, 0, 1 };
	sortuj_przez_wybieranie(t, 5);
	for(int i = 0; i < 5; ++i)
		std::cout << t[i] << std::endl;
	system("pause");
	return 0;
}


*/



/*
// Zadanie z kopcem
         90
     30      60
   17  15  20   8
 9               

0  1  2  3  4  5  6 7
90 30 60 17 15 20 8 9

int left(int i)   { return 2*i+1;   }
int right(int i)  { return 2*i+2;   }
int parent(int i) { return (i-1)/2; }


5 2 9 11 3 15 1

          5
	 3         1
  2       

Kopiec:             Posortowana tablica:
15 9 11 2 3 5 1     ---
11 9 5 2 3 1        15
9 3 5 2 1           11 15
5 3 1 2             9 11 15
*/


// Posortuj przez proste wstawianie
// Wejscie: 2 1 5 3 8 6 4 7
// 1 2 5 3 8 6 4 7
// 1 2 5 3 8 6 4 7
// 1 2 3 5 8 6 4 7
// 1 2 3 5 8 6 4 7
// 1 2 3 5 6 8 4 7
// 1 2 3 4 5 6 8 7
// 1 2 3 4 5 6 7 8


// Posortuj przez proste wybieranie
// Wejscie: 6 4 7 2 5 1 3 8
// 1 4 7 2 5 6 3 8
// 1 2 7 4 5 6 3 8
// 1 2 3 4 5 6 7 8
// 1 2 3 4 5 6 7 8
// 1 2 3 4 5 6 7 8
// 1 2 3 4 5 6 7 8
// 1 2 3 4 5 6 7 8

