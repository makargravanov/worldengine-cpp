#pragma once

class SQLocation {
private:
    long coordX, coordY;

public:
    explicit SQLocation(const long x, const long y) {
        coordX = x;
        coordY = y;
    }

    long x() const {
        return coordX;
    }

    long y() const {
        return coordY;
    }

    bool operator==(const SQLocation& o) const {
        return coordX == o.coordX && coordY == o.coordY;
    }
};
