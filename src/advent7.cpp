#include <iostream>
#include <fstream>
#include <string>
#include <inttypes.h>

#include "Gates.h"

static void process(const std::string& fname, const std::string& gate)
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

   uint16_t gate_value = g.getValue(gate);
   std::cout << "Gate " << gate << ": " << gate_value << std::endl;

   g.clear();
   g.setValue("b", gate_value);

   gate_value = g.getValue(gate);
   std::cout << "Gate " << gate << " updated: " << gate_value << std::endl;
}

int32_t main(int32_t argc, char **argv)
{
   if (argc != 3)
   {
      std::cerr << "usage: " << argv[0] << " <file name> <gate>" << std::endl;
      return 1;
   }

   const std::string fname(argv[1]);
   const std::string gate(argv[2]);
   std::cout << "Running: " << fname << std::endl;

   process(fname, gate);

   return 0;
}
