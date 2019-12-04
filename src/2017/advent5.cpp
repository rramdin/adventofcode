#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int jump(std::vector<int>& insts)
{
   long steps = 0;
   long current = 0;

   const int N = insts.size();

   while(current < N & current >= 0)
   {
      long offset = insts[current];
      insts[current] += 1 - 2*(offset>=3);
      current += offset;
      ++steps;
   }
   return steps;
}

int main(int argc, const char** argv)
{
   const std::string fname = argv[1];
   std::ifstream infile(fname);
   std::vector<int> instructions;
   int instruction;

   while(infile >> instruction)
   {
      instructions.push_back(instruction);
   }

   return jump(instructions);
}
