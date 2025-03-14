#include "AStarMemoryManager.h"
#include "SQLocation.h"
#include "SQMapHandler.h"
#include "Node.h"
#include "Path.h"
#include "AStar.h"

AStarMemoryManager* AStarMemoryManager::instance = nullptr;

void AStarMemoryManager::clear() noexcept {
    for (const auto element : instance->locations) {
        delete element;
    }
    for (const auto element : instance->handlers) {
        delete element;
    }
    for (const auto element : instance->nodes) {
        delete element;
    }
    for (const auto element : instance->pathVec) {
        delete element;
    }
    for (const auto element : instance->astarVec) {
        delete element;
    }
}