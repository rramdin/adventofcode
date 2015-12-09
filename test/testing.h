#include <iostream>

template <typename T1, typename T2>
void test(const std::string &name, T1 result, T2 expected)
{
   if (result == expected)
   {
      std::cerr << "PASS " << name << std::endl;
   }
   else
   {
      std::cerr << "FAIL " << name << " (got: " << result << "; expected: "
         << expected << ")" << std::endl;
      exit(1);
   }
}
