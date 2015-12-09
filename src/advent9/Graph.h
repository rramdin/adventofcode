#ifndef __GRAPH_H
#define __GRAPH_H

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
   uint64_t findShortestPath(Vertex *v, uint64_t distance,
                             std::set<Vertex*> &visited);

   std::map<std::string, Vertex*> graph_;
};

#endif
