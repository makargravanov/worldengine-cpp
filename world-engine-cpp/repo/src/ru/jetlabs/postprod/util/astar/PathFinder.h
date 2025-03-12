#pragma once
#include "AStar.h"
#include "Path.h"
#include "../numpysurrogate/arrays.h"

class PathFinder {
public:
    PathFinder() = default;

    static std::vector<std::pair<int,int>> find(const std::vector<std::vector<float>>& heightMap,
                                                const std::pair<int,int>& source,
                                                const std::pair<int,int>& destination) {

        const int sx = source.first;
        const int sy = source.second;
        const int dx = destination.first;
        const int dy = destination.second;
        std::vector<Node*> nodes = {};
        std::vector<std::pair<int,int>> path = {};
        const std::vector<float> flatHMap = flattenMatrix(heightMap);

        size_t width = 0;
        for (const auto& row : heightMap) {
            width = std::max(width, row.size());
        }
        AStar* pathfinder = new AStar(new SQMapHandler(flatHMap,
            static_cast<int>(heightMap.size()),
            static_cast<int>(width)));
        SQLocation* start = new SQLocation(sx,sy);
        SQLocation* end = new SQLocation(dx,dy);

        Path* p = pathfinder->findPath(start,end);
        if (p==nullptr) {
            
            return path;
        }
        for (const Node* node : p->getNodes()) {
            path.emplace_back(node->getLocation()->x(), node->getLocation()->y());
        }
        //delete pathfinder;
        //delete start;
        //delete end;
        //delete p;
        
        return path;
    }
};
