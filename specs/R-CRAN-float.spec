%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  float
%global packver   0.3-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          32-Bit Floats

License:          BSD 2-clause License + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-tools 

%description
R comes with a suite of utilities for linear algebra with "numeric"
(double precision) vectors/matrices. However, sometimes single precision
(or less!) is more than enough for a particular task.  This package
extends R's linear algebra facilities to include 32-bit float (single
precision) data. Float vectors/matrices have half the precision of their
"numeric"-type counterparts but are generally faster to numerically
operate on, for a performance vs accuracy trade-off.  The internal
representation is an S4 class, which allows us to keep the syntax
identical to that of base R's. Interaction between floats and base types
for binary operators is generally possible; in these cases, type promotion
always defaults to the higher precision.  The package ships with copies of
the single precision 'BLAS' and 'LAPACK', which are automatically built in
the event they are not available on the system.

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
test $(gcc -dumpversion) -ge 10 && mkdir -p ~/.R && echo "FFLAGS=$(R CMD config FFLAGS) -fallow-argument-mismatch" > ~/.R/Makevars
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
