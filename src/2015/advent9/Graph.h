#ifndef __GRAPH_H
#define __GRAPH_H

#include <functional>
#include <inttypes.h>
#include <map>
#include <set>
#include <string>

class Graph
{
public:
   void addEdge(const std::string &s);
   void addEdge(const std::string &v1, const std::string &v2, uint32_t weight);
   uint64_t findShortestPath();
   uint64_t findLongestPath();
private:
   class Vertex
   {
   public:
      Vertex(const std::string &name) : name_(name) {}
      void connect(Vertex* v, uint32_t weight);
      const std::string name_;
      std::map<Vertex*, uint32_t> edges_;
   };

   Vertex* getVertex(const std::string &v);

   uint64_t findPath(std::function<uint64_t(uint64_t,uint64_t)> fn);

   uint64_t findPath(Vertex *v, uint64_t distance,
                     std::set<Vertex*> &visited,
                     std::function<uint64_t(uint64_t,uint64_t)> fn);

   std::map<std::string, Vertex*> graph_;
};

#endif
