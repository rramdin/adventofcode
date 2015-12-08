#ifndef __GATES_H
#define __GATES_H

#include <string>
#include <map>
#include <inttypes.h>

class Gate;

class Gates
{
public:
   void process(const std::string &s);
   uint16_t getValue(const std::string &name) const;
   void clear();
   void setValue(const std::string &name, uint16_t value);
private:
   std::map<std::string, Gate*> gates_;
   mutable std::map<std::string, uint16_t> cache_;
};

class Gate
{
public:
   virtual uint16_t getValue(const Gates*) const = 0;
};

class ReferenceGate :public Gate
{
public:
   ReferenceGate(const std::string &name): name_(name) {}

   virtual uint16_t getValue(const Gates*) const override;
private:
   const std::string name_;
};

class AndGate :public Gate
{
public:
   AndGate(const std::string &g1, const std::string &g2)
      : g1_(g1), g2_(g2) {}

   virtual uint16_t getValue(const Gates*) const override;
private:
   const std::string g1_, g2_;
};

class OrGate :public Gate
{
public:
   OrGate(const std::string &g1, const std::string &g2)
      : g1_(g1), g2_(g2) {}

   virtual uint16_t getValue(const Gates*) const override;
private:
   const std::string g1_, g2_;
};

class LShiftGate :public Gate
{
public:
   LShiftGate(const std::string &g, const size_t shift)
      : g_(g), shift_(shift) {}

   virtual uint16_t getValue(const Gates*) const override;
private:
   const std::string g_;
   const size_t shift_;
};

class RShiftGate :public Gate
{
public:
   RShiftGate(const std::string &g, const size_t shift)
      : g_(g), shift_(shift) {}

   virtual uint16_t getValue(const Gates*) const override;
private:
   const std::string g_;
   const size_t shift_;
};

class NotGate :public Gate
{
public:
   NotGate(const std::string &g)
      : g_(g) {}

   virtual uint16_t getValue(const Gates*) const override;
private:
   const std::string g_;
};

#endif
