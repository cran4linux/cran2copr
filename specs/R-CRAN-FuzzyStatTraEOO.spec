%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FuzzyStatTraEOO
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Package 'FuzzyStatTra' in Encapsulated Object Oriented Programming

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-testthat 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-testthat 

%description
The aim of the package is to contain the package 'FuzzyStatTra' in
Encapsulated Object Oriented Programming using R6. 'FuzzyStatTra' contains
Statistical Methods for Trapezoidal Fuzzy Numbers, whose aim is to provide
some basic functions for doing statistical analysis with trapezoidal fuzzy
numbers. For more details, you can visit the website of the SMIRE+CoDiRE
(Statistical Methods with Imprecise Random Elements and Comparison of
Distributions of Random Elements) Research Group
(<https://bellman.ciencias.uniovi.es/smire+codire/>). The most related
paper can be found in References. Now, those functions are organized in
specific classes and methods. This object-based approach is an important
step in making statistical computing more accessible to users.

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
