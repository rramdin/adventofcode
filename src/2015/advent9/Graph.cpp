#include "Graph.h"

#include <boost/tokenizer.hpp>
#include <limits.h>

Graph::Vertex* Graph::getVertex(const std::string &v)
{
   Vertex *vertex = graph_[v];
   if (vertex == nullptr)
   {
      vertex = new Vertex(v);
      graph_[v] = vertex;
   }
   return vertex;
}

void Graph::Vertex::connect(Vertex* v, uint32_t weight)
{
   edges_[v] = weight;
}

void Graph::addEdge(const std::string &s)
{
   typedef boost::tokenizer<boost::char_separator<char>> tokenizer;
   static const boost::char_separator<char> sep(" \n");
   tokenizer tokens(s, sep);

   std::string v1, v2;
   uint32_t weight = 0;

   size_t index = 0;
   for (tokenizer::iterator i = tokens.begin(); i != tokens.end(); ++i)
   {
      std::string value(*i);
      switch (index)
      {
         case 0:
            v1 = *i;
            break;
         case 2:
            v2 = *i;
            break;
         case 4:
            weight = std::stoi(*i);
            break;
      }
      index++;
   }

   if (weight == 0)
   {
      throw("invalid specification: " + s);
   }

   addEdge(v1, v2, weight);
}

void Graph::addEdge(const std::string &v1, const std::string &v2,
                    uint32_t weight)
{
   Vertex *vertex1 = getVertex(v1);
   Vertex *vertex2 = getVertex(v2);
   vertex1->connect(vertex2, weight);
   vertex2->connect(vertex1, weight);
}

uint64_t Graph::findPath(Vertex *v, uint64_t distance,
                         std::set<Vertex*> &visited,
                         std::function<uint64_t(uint64_t,uint64_t)> fn)
{
   const auto& ins = visited.insert(v);
   bool found = false;
   uint64_t best = 0;
   for (auto& it : v->edges_)
   {
      if (visited.find(it.first) == visited.end())
      {
         uint64_t dist = findPath(it.first, distance + it.second, visited, fn);
         best = found ? fn(dist, best) : dist;
         found = true;
      }
   }
   visited.erase(ins.first);
   return best ? best : distance;
}

uint64_t Graph::findShortestPath() {
   auto l = [](uint64_t x, uint64_t y) { return x < y ? x : y; };
   return findPath(l);
}

uint64_t Graph::findLongestPath() {
   auto l = [](uint64_t x, uint64_t y) { return x > y ? x : y; };
   return findPath(l);
}

uint64_t Graph::findPath(std::function<uint64_t(uint64_t,uint64_t)> fn)
{
   std::set<Vertex*> visited;
   bool found = false;
   uint64_t best = 0;
   for (auto& it : graph_)
   {
      uint64_t dist = findPath(it.second, 0, visited, fn);
      best = found ? fn(dist, best) : dist;
      found = true;
   }
   return best;
}

