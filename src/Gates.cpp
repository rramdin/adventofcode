#include <boost/tokenizer.hpp>

#include "Gates.h"

void Gates::process(const std::string &s)
{
   typedef boost::tokenizer<boost::char_separator<char>> tokenizer;
   static const boost::char_separator<char> sep(" \n");
   tokenizer tokens(s, sep);

   std::string type, p1, p2, o;

   size_t index = 0;
   for (tokenizer::iterator i = tokens.begin(); i != tokens.end(); ++i)
   {
      std::string value(*i);
      if (index == 0)
      {
         if (value == "NOT")
         {
            type = value;
         }
         else
         {
            p1 = value;
         }
      }
      if (index == 1)
      {
         if (value == "AND" || value == "OR" ||
               value == "LSHIFT" || value == "RSHIFT")
         {
            type = value;
            ++i;
            p2 = *i;
            ++i;
            ++i;
            o = *i;
         }
         else if (value == "->")
         {
            type = "LITERAL";
            ++i;
            o = *i;
         }
         else // NOT
         {
            p1 = value;
            ++i;
            ++i;
            o = *i;
         }
         break;
      }
      index++;
   }
   Gate *g = nullptr;
   if (type == "LITERAL")
   {
      g = new LiteralGate(std::stoi(p1));
   }
   else if (type == "AND")
   {
      g = new AndGate(*gates_[p1], *gates_[p2]);
   }
   else if (type == "OR")
   {
      g = new OrGate(*gates_[p1], *gates_[p2]);
   }
   else if (type == "LSHIFT")
   {
      g = new LShiftGate(*gates_[p1], std::stoi(p2));
   }
   else if (type == "RSHIFT")
   {
      g = new RShiftGate(*gates_[p1], std::stoi(p2));
   }
   else if (type == "NOT")
   {
      g = new NotGate(*gates_[p1]);
   }
   gates_[o] = g;
}

uint16_t LiteralGate::getValue() const
{
   return value_;
}

uint16_t AndGate::getValue() const
{
   return g1_.getValue() & g2_.getValue();
}

uint16_t OrGate::getValue() const
{
   return g1_.getValue() | g2_.getValue();
}

uint16_t LShiftGate::getValue() const
{
   return g_.getValue() << shift_;
}

uint16_t RShiftGate::getValue() const
{
   return g_.getValue() >> shift_;
}

uint16_t NotGate::getValue() const
{
   return ~g_.getValue();
}

