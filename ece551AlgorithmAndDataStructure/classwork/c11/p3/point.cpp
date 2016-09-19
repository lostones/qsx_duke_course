#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include "point.h"

void Point::move( double dx, double dy )
{
	x=x+dx;
	y=y+dy;
}

double Point::distanceFrom( const Point & p)
{
	return sqrt( pow(x-p.x,2)+pow(y-p.y,2) );

}

double Point::getx() const
{
	return x;
}

double Point::gety() const
{
	return y;
}
