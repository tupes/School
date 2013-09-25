#ifndef RATIONAL_H
#define RATIONAL_H

// templated rational number class
// stores fractions num/den
// where num,den are integer variables of type T
//
// invariant: den > 0 && gcd(abs(num),den) = 1

#include <iostream>
#include <cassert>

template <typename T>
class Rational
{
public:
  
	// 0/1
	Rational();
	// num/1
	Rational(const T& num);
	// pre: den != 0,
	// set up num/den and normalize
	Rational(const T& num, const T& den);
	~Rational() { }

	// return numerator, denominator
	T get_num() const;
	T get_den() const;

	// return double approximation
	double value() const;

	// after each artithmetic operation the result needs to be normalized
	Rational operator+(const Rational &rhs) const;
	Rational operator-(const Rational &rhs) const;
	Rational operator*(const Rational &rhs) const;
	// pre: rhs != 0
	Rational operator/(const Rational &rhs) const;

	Rational &operator+=(const Rational &rhs);
	Rational &operator-=(const Rational &rhs);
	Rational &operator*=(const Rational &rhs);
	// pre: rhs != 0
	Rational &operator/=(const Rational &rhs);

	// pre/post increment/decrement operators
	Rational &operator++();
	Rational &operator--();
	Rational operator++(int);
	Rational operator--(int);

private:
	// the numerator and denominator of the rational number
	T num, den;
	// pre-cond: den != 0
	// change num/den such that den > 0,
	// and num and den have no commmon factor > 1
	void normalize();

	// return greatest common divisor of a and b
	// (Euclid's algorithm)
	// pre-cond: a, b > 0
	T gcd(T a, T b);
};

// writes [num/den] to os
template <typename T>
std::ostream &operator<<(std::ostream &os, const Rational<T> &r) {
	return os << "[" << r.get_num() << "/" << r.get_den() << "]";
}

template <typename T>
Rational<T>::Rational() {
	num = 0;
	den = 1;
}

template <typename T>
Rational<T>::Rational(const T& n) {
	num = n;
	den = 1;
}

template <typename T>
Rational<T>::Rational(const T& n, const T& d) {
	num = n;
	den = d;
	normalize();
}

template <typename T>
T Rational<T>::get_num() const {
	return num;
}

template <typename T>
T Rational<T>::get_den() const {
	return den;
}

// return a double approximation to rational number
template <typename T>
double Rational<T>::value() const {
	return (double)num / den;
}

template <typename T>
Rational<T> Rational<T>::operator+(const Rational<T> &rhs) const {
	T d = den * rhs.den;
	T multiple = d / den;
	T left_num = num * multiple;
	multiple = d / rhs.den;
	T right_num = rhs.num * multiple;
	return Rational<T>(left_num + right_num, d);
}

template <typename T>
Rational<T> Rational<T>::operator-(const Rational<T> &rhs) const {
	T d = den * rhs.den;
	T multiple = d / den;
	T left_num = num * multiple;
	multiple = d / rhs.den;
	T right_num = rhs.num * multiple;
	return Rational<T>(left_num - right_num, d);
}

template <typename T>
Rational<T> Rational<T>::operator*(const Rational<T> &rhs) const {
	return Rational<T>(num * rhs.num, den * rhs.den);
}

template <typename T>
Rational<T> Rational<T>::operator/(const Rational<T> &rhs) const {
	assert(rhs.num != 0);
	return Rational<T>(num * rhs.den, den * rhs.num);
}

template <typename T>
Rational<T>& Rational<T>::operator+=(const Rational<T> &rhs) {
	T d = den * rhs.den;
	T multiple = d / den;
	T left_num = num * multiple;
	multiple = d / rhs.den;
	T right_num = rhs.num * multiple;
	num = left_num + right_num;
	den = d;
	normalize();
	return *this;
}

template <typename T>
Rational<T>& Rational<T>::operator-=(const Rational<T> &rhs) {
	T d = den * rhs.den;
	T multiple = d / den;
	T left_num = num * multiple;
	multiple = d / rhs.den;
	T right_num = rhs.num * multiple;
	num = left_num - right_num;
	den = d;
	normalize();
	return *this;
}

template <typename T>
Rational<T>& Rational<T>::operator*=(const Rational<T> &rhs) {
	num *= rhs.num;
	den *= rhs.den;
	normalize();
	return *this;
}

template <typename T>
Rational<T>& Rational<T>::operator/=(const Rational<T> &rhs) {
	assert(rhs.num != 0);
	num *= rhs.den;
	den *= rhs.num;
	normalize();
	return *this;
}

template <typename T>
Rational<T>& Rational<T>::operator++() {
	*this += Rational<T>(1);
	return *this;
}

template <typename T>
Rational<T>& Rational<T>::operator--() {
	*this -= Rational<T>(1);
	return *this;
}

template <typename T>
Rational<T> Rational<T>::operator++(int) {
	Rational<T> ret(*this);
	++*this;
	return ret;
}

template <typename T>
Rational<T> Rational<T>::operator--(int) {
	Rational<T> ret(*this);
	--*this;
	return ret;
}

// make sure the denominator isn't 0 or negative, and the rational number
// is reduced to its lowest terms
template <typename T>
void Rational<T>::normalize() {
	assert(den != 0);
	if (den < 0) {
		num *= -1;
		den *= -1;
	}
	T factor;
	if (num < 0)
		factor = gcd(num * -1, den);
	else
		factor = gcd(num, den);
	num /= factor;
	den /= factor;
}

// Euclid's greatest common denominator algorithm, taken from Wikipedia
template <typename T>
T Rational<T>::gcd(T a, T b) {
	assert(a > 0); assert(b > 0);
	T temp;
	while (b != 0) {
		temp = b;
		b = a % b;
		a = temp;
	}
	return a;
}

#endif
