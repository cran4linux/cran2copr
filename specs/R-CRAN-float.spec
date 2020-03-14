%global packname  float
%global packver   0.2-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}
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

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install
test $(gcc -dumpversion) -ge 10 && mkdir -p ~/.R && echo "FFLAGS=$(R CMD config FFLAGS) -fallow-argument-mismatch" > ~/.R/Makevars
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/benchmarks
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
