%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  contFracR
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Continued Fraction Generators and Evaluators

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rmpfr 
BuildRequires:    R-CRAN-go2bigq 
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rmpfr 
Requires:         R-CRAN-go2bigq 
Requires:         R-CRAN-gmp 
Requires:         R-methods 

%description
Converts numbers to continued fractions and back again. A solver for
Pell's Equation is provided.  The method for calculating roots in
continued fraction form is provided without published attribution in such
places as Professor Emeritus Jonathan Lubin,
<http://www.math.brown.edu/jlubin/> and his post to StackOverflow,
<https://math.stackexchange.com/questions/2215918> , or Professor Ron
Knott, e.g., <https://r-knott.surrey.ac.uk/Fibonacci/cfINTRO.html> .

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
