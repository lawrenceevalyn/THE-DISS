//-----------------------------------------------------------
//  Purpose:    Header file for the List class.
//  Author:     John Gauch
//-----------------------------------------------------------

#include <iostream>
#include <fstream>
using namespace std;

//-----------------------------------------------------------
// List data node definition
//-----------------------------------------------------------
class LNode
{
 public:
   string Value;
   LNode *Next;
};

//-----------------------------------------------------------
// Define the List class interface 
//-----------------------------------------------------------
class List
{
 public:
   // Constructors
   List();
   List(const List & list);
    ~List();

   // Methods
   bool InsertHead(string value);
   bool InsertTail(string value);
   bool Search(string value);
   string GetFirst();
   bool Delete(string value);
   void Print(ofstream &Dout);
   void Print();
   bool IsEmpty();

 private:
     LNode * Head;
};
