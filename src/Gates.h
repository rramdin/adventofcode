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

private:
   std::map<std::string, Gate*> gates_;

};

class Gate
{
public:
   virtual uint16_t getValue() const = 0;
};

class LiteralGate :public Gate
{
public:
   LiteralGate(uint16_t value): value_(value) {}

   virtual uint16_t getValue() const override;
private:
   uint16_t value_;
};

class AndGate :public Gate
{
public:
   AndGate(const Gate &g1, const Gate &g2)
      : g1_(g1), g2_(g2) {}

   virtual uint16_t getValue() const override;
private:
   const Gate &g1_, &g2_;
};

class OrGate :public Gate
{
public:
   OrGate(const Gate &g1, const Gate &g2)
      : g1_(g1), g2_(g2) {}

   virtual uint16_t getValue() const override;
private:
   const Gate &g1_, &g2_;
};

class LShiftGate :public Gate
{
public:
   LShiftGate(const Gate &g, const size_t shift)
      : g_(g), shift_(shift) {}

   virtual uint16_t getValue() const override;
private:
   const Gate &g_;
   const size_t shift_;
};

class RShiftGate :public Gate
{
public:
   RShiftGate(const Gate &g, const size_t shift)
      : g_(g), shift_(shift) {}

   virtual uint16_t getValue() const override;
private:
   const Gate &g_;
   const size_t shift_;
};

class NotGate :public Gate
{
public:
   NotGate(const Gate &g)
      : g_(g) {}

   virtual uint16_t getValue() const override;
private:
   const Gate &g_;
};

#endif
