#include <iostream>
#include <fstream>
#include <string>
#include <inttypes.h>

#include "Gates.h"

static void readFile(const std::string& fname)
{
   Gates g;

   std::string line;
   std::ifstream file(fname);
   if (file.is_open())
   {
      while (std::getline(file, line))
      {
         if (line.size())
         {
            g.process(line);
         }
      }
   }
}

int32_t main(int32_t argc, char **argv)
{
   if (argc < 2)
   {
      std::cerr << "usage: " << argv[0] << " <file name>" << std::endl;
      return 1;
   }

   const std::string fname(argv[1]);
   std::cout << "running: " << fname << std::endl;

   readFile(fname);

   return 0;
}
