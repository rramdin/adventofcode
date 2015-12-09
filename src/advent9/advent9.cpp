#include <iostream>
#include <fstream>
#include <string>
#include <inttypes.h>

#include "Graph.h"

static void process(const std::string& fname)
{
   Graph g;

   std::string line;
   std::ifstream file(fname);
   if (file.is_open())
   {
      while (std::getline(file, line))
      {
         if (line.size())
         {
            g.addEdge(line);
         }
      }
   }

   uint64_t shortest = g.findShortestPath();
   std::cout << "Shortest path: " << shortest << std::endl;
}

int32_t main(int32_t argc, char **argv)
{
   if (argc != 2)
   {
      std::cerr << "usage: " << argv[0] << " <file name>" << std::endl;
      return 1;
   }

   const std::string fname(argv[1]);
   std::cout << "Running: " << fname << std::endl;

   process(fname);

   return 0;
}
