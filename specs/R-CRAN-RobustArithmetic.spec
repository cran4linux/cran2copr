%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RobustArithmetic
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Verified Interval Arithmetic with Correctly Rounded Kernels

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Verified interval arithmetic for R, in the inf-sup (endpoint)
representation of the set-based flavor of the interval standard. Every
operation returns an enclosure that provably contains the exact result:
outward rounding is obtained from the predecessor and successor formulas
of Rump, Zimmermann, Boldo and Melquiond (2009)
<doi:10.1007/s10543-009-0218-z>, which are valid under round-to-nearest
and therefore need no change to the floating-point rounding mode. That
mode is not reachable from R, and changing it would not be a local act: it
is per-thread state of the processor, so it would govern every
floating-point operation executed afterwards on that thread, in this
package or anywhere else. Elementary functions are provided at two levels:
a fast level over the included correctly rounded binary64 implementation,
comprising fifteen kernels from CORE-MATH
<doi:10.1109/ARITH54963.2022.00014> and the hardware square root, widened
by the pre-registered slack of two outward steps; and a rigorous level
over 'Rmpfr' with a directed-rounding bridge, reached by an escalation
ladder of precisions when a verdict would otherwise fall inside the slack.
Fast-level enclosures retain measured provenance because correct rounding
of the included software is verified numerically rather than established
here as a theorem for every kernel. On top of the kernel the package
builds natural and centered interval extensions of expressions, a
monotonicity test, the Hansen-Sengupta interval Newton operator with
extended division and epsilon-inflated candidate verification, and a
subdivision (paving) engine whose only failure mode is a named abstention
with its budget printed. Conformance with IEEE Std 1788.1-2017
<doi:10.1109/IEEESTD.2018.8277144> is not claimed, and the reason is the
standard's own: its subclause 1.5 makes conformance a list of requirements
that an implementation shall satisfy, with no partial grade to claim. What
this package follows, measured one requirement at a time and stated in the
package documentation, is the interval type and the decoration system of
clause 5, 22 of the 39 arithmetic operations of Table 4.1, and the seven
numeric functions of Table 4.3. What it does not provide is the
cancellative operations, the interval comparison relations, the text input
and output of subclause 6.8, the interchange representation of subclause
7.3, and the tightest accuracy that subclause 6.5.2 requires of the basic
operations, which here are one unit in the last place wider at each end.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
