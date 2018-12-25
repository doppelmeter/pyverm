from numbers import Real
import re
import decimal


class DecimalNumber(Real):
    exp = -20
    __slots__ = ('_value', '_sign')

    def __new__(cls, value="0"):
        self = object.__new__(cls)

        if isinstance(value, int):
            if value >= 0:
                self._sign = 0
            else:
                self._sign = 1
            self._value = str(abs(value))+("0"*abs(self.exp))

            return self

        if isinstance(value, float):
            if value >= 0:
                self._sign = 0
            else:
                self._sign = 1
            integer = int(value)
            after_that = int((value - integer)*10**20)
            self._value = str(integer)+str(after_that)[0:20]

            return self

        if isinstance(value, decimal.Decimal):
            if value >= 0:
                self._sign = 0
            else:
                self._sign = 1
            string = str(value)
            self = DecimalNumber(string)

            return self



        ############################################################################################
        # for strings copied from decimal
        ############################################################################################
        if isinstance(value, str):
            ########################################################################################
            _parser = re.compile(r"""        # A numeric string consists of:
                    #    \s*
                        (?P<sign>[-+])?              # an optional sign, followed by either...
                        (
                            (?=\d|\.\d)              # ...a number (with at least one digit)
                            (?P<int>\d*)             # having a (possibly empty) integer part
                            (\.(?P<frac>\d*))?       # followed by an optional fractional part
                            (E(?P<exp>[-+]?\d+))?    # followed by an optional exponent, or...
                        |
                            Inf(inity)?              # ...an infinity, or...
                        |
                            (?P<signal>s)?           # ...an (optionally signaling)
                            NaN                      # NaN
                            (?P<diag>\d*)            # with (possibly empty) diagnostic info.
                        )
                    #    \s*
                        \Z
                    """, re.VERBOSE | re.IGNORECASE).match
            ##########################################################################################
            m = _parser(value.strip())


            if m.group('sign') == "-":
                self._sign = 1
            else:
                self._sign = 0

            intpart = m.group('int')
            if intpart is not None:
                # finite number
                fracpart = m.group('frac') or ''
                exp = int(m.group('exp') or '0')

                value_after =  fracpart + ("0"*(self.exp-len(fracpart)))
                self._value = intpart + value_after[:20]

            return self





    def __str__(self):
        sign = ['', '-'][self._sign]
        leftdigits = int(self.exp) + len(self._value)
        dotplace = leftdigits

        string = sign+self._value[:(len(self._value)+self.exp)]+'.' + self._value[(len(self._value)+self.exp):]
        return str(string)


    def __complex__(self):
        """Return a builtin complex instance. Called for complex(self)."""

    def __bool__(self):
        """True if self != 0. Called for bool(self)."""
        return self != 0

    @property
    def real(self):
        """Retrieve the real component of this number.
        This should subclass Real.
        """
        raise NotImplementedError

    @property
    def imag(self):
        """Retrieve the imaginary component of this number.
        This should subclass Real.
        """
        raise NotImplementedError


    def __add__(self, other):
        """self + other"""
        self_ = decimal.Decimal(str(self))
        other = decimal.Decimal(str(other))
        res = self_ + other
        return DecimalNumber(str(res))


    def __radd__(self, other):
        """other + self"""
        return self.__add__(self.conjugate())



    def __neg__(self):
        """-self"""
        self_ = decimal.Decimal(str(self))
        res = -self_
        return DecimalNumber(str(res))


    def __pos__(self):
        """+self"""
        self_ = decimal.Decimal(str(self))
        res = +self_
        return DecimalNumber(str(res))

    def __sub__(self, other):
        """self - other"""
        return self + -other

    def __rsub__(self, other):
        """other - self"""
        return -self + other


    def __mul__(self, other):
        """self * other"""
        self_ = decimal.Decimal(str(self))
        other = decimal.Decimal(str(other))
        res = self_ * other
        return DecimalNumber(str(res))


    def __rmul__(self, other):
        """other * self"""
        self_ = decimal.Decimal(str(self))
        other = decimal.Decimal(str(other))
        res = other * self_
        return DecimalNumber(str(res))


    def __truediv__(self, other):
        """self / other: Should promote to float when necessary."""
        self_ = decimal.Decimal(str(self))
        other = decimal.Decimal(str(other))
        res = self_ / other
        return DecimalNumber(str(res))


    def __rtruediv__(self, other):
        """other / self"""
        self_ = decimal.Decimal(str(self))
        other = decimal.Decimal(str(other))
        res = other / self_
        return DecimalNumber(str(res))


    def __pow__(self, exponent):
        """self**exponent; should promote to float or complex when necessary."""
        self_ = decimal.Decimal(str(self))
        other = decimal.Decimal(str(exponent))
        res = self_ ** other
        return DecimalNumber(str(res))


    def __rpow__(self, base):
        """base ** self"""
        self_ = decimal.Decimal(str(self))
        other = decimal.Decimal(str(base))
        res =  other ** self_
        return DecimalNumber(str(res))


    def __abs__(self):
        """Returns the Real distance from 0. Called for abs(self)."""
        self_ = decimal.Decimal(str(self))
        res = abs(self_)
        return DecimalNumber(str(res))


    def conjugate(self):
        """(x+y*i).conjugate() returns (x-y*i)."""
        raise NotImplementedError


    def __eq__(self, other):
        """self == other"""
        self_ = decimal.Decimal(str(self))
        other = decimal.Decimal(str(float(other)))
        return self_ == other

    def __float__(self):
        """Any Real can be converted to a native float object.
        Called for float(self)."""
        return float(str(decimal.Decimal(str(self))))


    def __trunc__(self):
        """trunc(self): Truncates self to an Integral.
        Returns an Integral i such that:
          * i>0 iff self>0;
          * abs(i) <= abs(self);
          * for any Integral j satisfying the first two conditions,
            abs(i) >= abs(j) [i.e. i has "maximal" abs among those].
        i.e. "truncate towards 0".
        """
        raise NotImplementedError


    def __floor__(self):
        """Finds the greatest Integral <= self."""
        raise NotImplementedError


    def __ceil__(self):
        """Finds the least Integral >= self."""
        raise NotImplementedError


    def __round__(self, ndigits=None):
        """Rounds self to ndigits decimal places, defaulting to 0.
        If ndigits is omitted or None, returns an Integral, otherwise
        returns a Real. Rounds half toward even.
        """
        raise NotImplementedError

    def __divmod__(self, other):
        """divmod(self, other): The pair (self // other, self % other).
        Sometimes this can be computed faster than the pair of
        operations.
        """
        return (self // other, self % other)

    def __rdivmod__(self, other):
        """divmod(other, self): The pair (self // other, self % other).
        Sometimes this can be computed faster than the pair of
        operations.
        """
        return (other // self, other % self)


    def __floordiv__(self, other):
        """self // other: The floor() of self/other."""
        raise NotImplementedError


    def __rfloordiv__(self, other):
        """other // self: The floor() of other/self."""
        raise NotImplementedError


    def __mod__(self, other):
        """self % other"""
        self_ = decimal.Decimal(str(self))
        other = decimal.Decimal(str(float(other)))
        res = self_ % other
        return DecimalNumber(str(res))


    def __rmod__(self, other):
        """other % self"""
        self_ = decimal.Decimal(str(self))
        other = decimal.Decimal(str(float(other)))
        res = other % self_
        return DecimalNumber(str(res))


    def __lt__(self, other):
        """self < other
        < on Reals defines a total ordering, except perhaps for NaN."""
        self_ = decimal.Decimal(str(self))
        other = decimal.Decimal(str(other))
        return self_ < other

    def __gt__(self, other):
        self_ = decimal.Decimal(str(self))
        other = decimal.Decimal(str(other))
        return self_ > other


    def __le__(self, other):
        """self <= other"""
        self_ = decimal.Decimal(str(self))
        other = decimal.Decimal(str(other))
        return self_ <= other

    # Concrete implementations of Complex abstract methods.
    def __complex__(self):
        """complex(self) == complex(float(self), 0)"""
        return complex(float(self))


    def real(self):
        """Real numbers are their real component."""
        return +self

    @property
    def imag(self):
        """Real numbers have no imaginary component."""
        return 0

    def conjugate(self):
        """Conjugate is a no-op for Reals."""
        return +self

    def __int__(self):
        f = float(str(self))
        return int(f)

    @property
    def is_nan(self):
        return False

    def is_nan(self):
        return False



Real.register(DecimalNumber)

