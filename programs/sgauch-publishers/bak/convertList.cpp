//----------------------------------------------------
// Author:     Susan Gauch
//----------------------------------------------------
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <string>
#include "list.h"
#include "hashtable.h"
using namespace std;

int NumPubs = 0;

// Remove Trailing and Leading spaces
string Process(char *Token)
{
int Start = 0;
int End = strlen(Token)-1;
string Raw = Token;
string Trimmed;

   while (Token[Start] == ' ')
      Start++;
   while (Token[End] == ' ')
      End--;
   
   Trimmed = Raw.substr(Start, End-Start+1);
   return Trimmed;
}

// Parse the input file and put the tokens in Publishers
void ParseInput (ifstream &Din, List Publishers[])
{
char Line[500];
char *Token;
char s[2] = ";";
string StrToken;

   Din.getline (Line, 500);
   while (!Din.eof())
   {
      // Split on ;
      Token = strtok(Line, s);
      while (Token != NULL)
      {
         StrToken = Process(Token);
         (Publishers[NumPubs]).InsertTail(StrToken);
         Token = strtok(NULL, s);
      }
      NumPubs++;
      Din.getline (Line, 500);
   }
      cout << "NumPubs: " << NumPubs << endl;
}

//Apply the mappings in the HT to the Publishers
void ApplyMappings (List Publishers[], HashTable MapHT, List ShortPubs[])
{
string Token;

   for (int i=0; i<NumPubs; i++)
   {
      Token = (Publishers[i]).GetFirst();
      (ShortPubs[i]).InsertHead(Token);
   }
}

//Output the publishers in csv format
void OutputPubs (ofstream &Dout, List Publishers[], List ShortPubs[])
{
   for (int i=0; i<NumPubs; i++)
   {
      (ShortPubs[i]).Print(Dout);
      Dout << ",";
      (Publishers[i]).Print(Dout);
      Dout << ",\n";
   }
}

int main()
{
ifstream Din;
ifstream Dmapin;
ofstream Dmapout;
ofstream Dout;
string FilenameRoot;
string Filename;
List Publishers[40000];
List ShortPubs[40000];
HashTable MapHT(40000);
 
   // Open all the files
   cout << "Takes as input two files:\n";
   cout << "   XXX_in.txt (list of publisher names to convert)\n";
   cout << "   XXX_map_in.csv (list of mappings of publisher names to short names)\n";
   cout << "It produces two files: \n";
   cout << "   XXX_out.csv (a two column csv file with original name and short name)\n";
   cout << "   XXX_map_out.csv (mappings file updated with newly discovered mappings added)\n";
   cout << "Enter filename root to convert (i.e., just the XXX part):  ";
   cin >> FilenameRoot;
   
   Filename = FilenameRoot + "_in.txt";
   Din.open (Filename.c_str());
   if (!Din)
   {
      cout << "Could not open " << Filename << endl;
      exit (EXIT_FAILURE);
   }
   Filename = FilenameRoot + "_map_in.csv";
   Dmapin.open (Filename.c_str());
   if (!Dmapin)
   {
      cout << "Could not open " << Filename << endl;
      exit (EXIT_FAILURE);
   }
   Filename = FilenameRoot + "_out.csv";
   Dout.open (Filename.c_str());
   if (!Dout)
   {
      cout << "Could not open " << Filename << endl;
      exit (EXIT_FAILURE);
   }
   Filename = FilenameRoot + "_map_out.csv";
   Dmapout.open (Filename.c_str());
   if (!Dmapout)
   {
      cout << "Could not open " << Filename << endl;
      exit (EXIT_FAILURE);
   }

   ParseInput (Din, Publishers);
   // GetMappings (Dmapin, MapHT);
   ApplyMappings (Publishers, MapHT, ShortPubs);
   OutputPubs (Dout, Publishers, ShortPubs);
   //  OuputMappings(Dmapout, MapHT);

   // Close all the files
   Din.close();
   Dmapin.close();
   Dout.close();
   Dmapout.close();
   
return 0;
}
