//----------------------------------------------------
// Author:     Susan Gauch
//----------------------------------------------------
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include "hashtable.h"
using namespace std;

const int NUM_PUBS=30000;
typedef std::vector<string> str_vec_t;

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

// Initialize the single token word mappings hashtable
void Init(ifstream &Dwordmapin, HashTable &WordmapHT)
{
char Line[500];
char s[2] = ",";
char* Original;
char* Substitution;

   // Init from known mappings
   Dwordmapin.getline (Line, 500);
   while (!Dwordmapin.eof())
   {
      // Split on ,
      Original = strtok(Line, s);
      Substitution = strtok(NULL, s);
      WordmapHT.Insert(Original, Substitution);  // maps from long to short
      Dwordmapin.getline (Line, 500);
   }
}

void RemoveStopwords (HashTable &WordmapHT, string StrToken, string &NewToken)
{
char Token[1000];
char Temp[1000];
string Substitution;
unsigned int i = 0;
unsigned int j;

   NewToken = "";
   strcpy (Temp, StrToken.c_str());
   while (i < strlen(Temp))
   {
      // get a space delimited token
      j=0;
      while (i < strlen(Temp) && Temp[i] != ' ')
      {
         Token[j] = Temp[i];
         i++;
         j++;
      }
      Token[j]='\0';
      i++;
      // check to see if token is a stopword
      Substitution = WordmapHT.GetData(Token);

      // if not a stopword, add to NewToken
      if (Substitution != "NULL")
      {
         if (NewToken.length() != 0)
            NewToken = NewToken + " ";
         if (Substitution == "")
            NewToken = NewToken + Token;
         else
            NewToken = NewToken + Substitution;
      }
   }
}

// Parse the input file and put the tokens in Publishers
void ParseInput (ifstream &Din, ifstream &Dwordmapin, str_vec_t LongPubs[NUM_PUBS], str_vec_t Publishers[NUM_PUBS])
{
char Line[500];
char *Token;
char s[2] = ";";
string StrToken;
string NewToken;
HashTable WordmapHT(1000);

   Init(Dwordmapin, WordmapHT);
   Din.getline (Line, 500);
   while (!Din.eof())
   {
      // Split on ;
      Token = strtok(Line, s);
      while (Token != NULL)
      {
         // remove blanks
         StrToken = Process(Token);
         (LongPubs[NumPubs]).push_back(StrToken);

         // remove stopwords
         RemoveStopwords (WordmapHT, StrToken, NewToken); 
         if (NewToken != "")
            (Publishers[NumPubs]).push_back(NewToken);

         // get the next token
         Token = strtok(NULL, s);
      }
      NumPubs++;
      Din.getline (Line, 500);
      if (NumPubs%100 == 0)
         cout << NumPubs << ": " << Line << endl;
   }
   cout << "NumPubs: " << NumPubs << endl;
}

// Fill the Mappings table
void GetMappings (ifstream &Dnamemapin, HashTable &MapHT)
{
char Line[500];
char *Token;
char s[2] = ";";
string Short;
string Long;

   // Init from known mappings
   Dnamemapin.getline (Line, 500);
   while (!Dnamemapin.eof())
   {
      // Split on ,
      Token = strtok(Line, s);
      Long = Process(Token);
      Token = strtok(NULL, s);
      Short = Process(Token);
      MapHT.Insert(Long, Short); 
      Dnamemapin.getline (Line, 500);
   }
}

//Apply the mappings in the HT to the Publishers
void ApplyMappings (str_vec_t Publishers[NUM_PUBS], HashTable &MapHT, str_vec_t ShortPubs[NUM_PUBS])
{
string Long;
string Short;

   // loop over publishers
   for (int i=0; i<NumPubs; i++)
   {
      // loop over names in publishers
      for (unsigned int j=0; j<(Publishers[i]).size(); j++)
      {
         Long = Publishers[i][j];
         Short = MapHT.GetData(Long);
         if (Short == "")
            Short = Long;
         if (Short != "NULL")
            (ShortPubs[i]).push_back(Short);
      }
   }
}

//Output the publishers in csv format
void OutputPubs (ofstream &Dout, str_vec_t Publishers[NUM_PUBS], str_vec_t ShortPubs[NUM_PUBS])
{
bool FirstTime;

   for (int i=0; i<NumPubs; i++)
   {
      // Print the short publisher
      // loop over tokens
      FirstTime = true;
      for (unsigned int j=0; j<(Publishers[i]).size(); j++)
      {
         if (FirstTime)
            FirstTime = false;
         else
            Dout << " ; ";
         Dout << Publishers[i][j];
      }
      Dout << ",";

      // Print the long publisher
      // loop over tokens
      FirstTime = true;
      for (unsigned int j=0; j<(ShortPubs[i]).size(); j++)
      {
         if (FirstTime)
            FirstTime = false;
         else
            Dout << " ; ";
         Dout << ShortPubs[i][j];
      }
      Dout << ",\n";
   }
}

int main()
{
ifstream Din;
ifstream Dnamemapin;
ifstream Dwordmapin;
ofstream Dout;
ofstream Dmapout;
string InFilename = "in.txt";
string WordMapFilename = "wordmap.csv";
string NameMapFilename = "namemap.txt";
string OutFilename = "out.csv";
str_vec_t LongPubs[NUM_PUBS];
str_vec_t Publishers[NUM_PUBS];
str_vec_t ShortPubs[NUM_PUBS];
HashTable MapHT(NUM_PUBS);
 
   // Open all the files
   cout << "Takes as input three files:\n";
   cout << "   in.txt (long publisher names to convert)\n";
   cout << "   wordmap.csv (mappings of single words to other words or NULL, separated by ,)\n";
   cout << "   namemap.txt (mappings of publisher names to short names or NULL, separated by ;)\n";
   cout << "It produces an output file: \n";
   cout << "   out.csv (mappings of original long names to short names, separated by commas)\n";
   
   Din.open (InFilename.c_str());
   if (!Din)
   {
      cout << "Could not open " << InFilename << endl;
      exit (EXIT_FAILURE);
   }
   Dwordmapin.open (WordMapFilename.c_str());
   if (!Dwordmapin)
   {
      cout << "Could not open " << WordMapFilename << endl;
      exit (EXIT_FAILURE);
   }
   Dnamemapin.open (NameMapFilename.c_str());
   if (!Dnamemapin)
   {
      cout << "Could not open " << NameMapFilename << endl;
      exit (EXIT_FAILURE);
   }
   Dout.open (OutFilename.c_str());
   if (!Dout)
   {
      cout << "Could not open " << OutFilename << endl;
      exit (EXIT_FAILURE);
   }

   ParseInput (Din, Dwordmapin, LongPubs, Publishers);
   GetMappings (Dnamemapin, MapHT);
   ApplyMappings (Publishers, MapHT, ShortPubs);
   OutputPubs (Dout, LongPubs, ShortPubs);

//   Filename = FilenameRoot + "_map.csv";
//   MapHT.Print(Filename.c_str());

   // Close all the files
   Din.close();
   Dnamemapin.close();
   Dout.close();
   
return 0;
}
