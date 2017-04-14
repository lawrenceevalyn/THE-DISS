/* Filename:  hashtable.h
 * Author:    Susan Gauch
 * Date:      2/25/10
 * Purpose:   The header file for a hash table of strings and strings. 
*/

using namespace std;

class HashTable {
public:
   HashTable (const HashTable& ht );       // constructor for a copy
   HashTable(const unsigned long NumKeys);          // constructor of hashtable 
   ~HashTable();                           // destructor
   void Print (const char *filename) const;       
   void Insert (const string Key, const string Data); 
   string GetData (const string Key); 
   void GetUsage (int &Used, int &Collisions, int &Lookups) const;
protected:
   struct StringStringPair // the datatype stored in the hashtable`
   {
      string key;
      string data;
   };
   unsigned long Find (const string Key); // the index of the ddr in the hashtable
private:
   StringStringPair *hashtable;        // the hashtable array itself
   unsigned long size;              // the hashtable size
   unsigned long used;
   unsigned long collisions;
   unsigned long lookups;
};
