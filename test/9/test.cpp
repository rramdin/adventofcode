#include "../../src/advent9/Graph.h"
#include "../testing.h"

int main(int argc, char **argv)
{
   Graph g;
   g.addEdge("London to Dublin = 464");
   g.addEdge("London to Belfast = 518");
   g.addEdge("Dublin to Belfast = 141");

   test("findShortestPath", g.findShortestPath(), 605);
   test("findLongestPath", g.findLongestPath(), 982);
}
