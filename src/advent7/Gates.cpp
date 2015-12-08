#include <boost/tokenizer.hpp>

#include "Gates.h"

void Gates::clear()
{
   cache_.clear();
}

void Gates::setValue(const std::string &name, uint16_t value)
{
   cache_[name] = value;
}

uint16_t Gates::getValue(const std::string &name) const
{
   const auto& hit = cache_.find(name);
   if (hit != cache_.end())
   {
      return hit->second;
   }

   uint16_t value = 0;
   try
   {
      value= std::stoi(name);
   }
   catch (std::invalid_argument e)
   {
      const auto& it = gates_.find(name);
      if (it != gates_.end())
      {
         value = it->second->getValue(this);
      }
   }

   cache_[name] = value;

   return value;
}

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
      g = new ReferenceGate(p1);
   }
   else if (type == "AND")
   {
      g = new AndGate(p1, p2);
   }
   else if (type == "OR")
   {
      g = new OrGate(p1, p2);
   }
   else if (type == "LSHIFT")
   {
      g = new LShiftGate(p1, std::stoi(p2));
   }
   else if (type == "RSHIFT")
   {
      g = new RShiftGate(p1, std::stoi(p2));
   }
   else if (type == "NOT")
   {
      g = new NotGate(p1);
   }
   gates_[o] = g;
}


#define VAL(x) gates->getValue(((x)))

uint16_t ReferenceGate::getValue(const Gates* gates) const
{
   return VAL(name_);
}

uint16_t AndGate::getValue(const Gates* gates) const
{
   return VAL(g1_) & VAL(g2_);
}

uint16_t OrGate::getValue(const Gates* gates) const
{
   return VAL(g1_) | VAL(g2_);
}

uint16_t LShiftGate::getValue(const Gates* gates) const
{
   return VAL(g_) << shift_;
}

uint16_t RShiftGate::getValue(const Gates* gates) const
{
   return VAL(g_) >> shift_;
}

uint16_t NotGate::getValue(const Gates* gates) const
{
   return ~VAL(g_);
}

