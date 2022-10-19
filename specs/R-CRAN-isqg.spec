%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  isqg
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          In Silico Quantitative Genetics

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildRequires:    R-CRAN-R6 >= 2.5.0
BuildRequires:    R-CRAN-Rdpack >= 2.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.6
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-R6 >= 2.5.0
Requires:         R-CRAN-Rdpack >= 2.1
Requires:         R-CRAN-Rcpp >= 1.0.6
Requires:         R-methods 

%description
Accomplish high performance simulations in quantitative genetics. The
molecular genetic components are represented by R6/C++ classes and
methods. The core computational algorithm is implemented using bitsets
according to <doi:10.1534/g3.119.400373>. A mix between low and high level
interfaces provides great flexibility and allows user defined extensions
and a wide range of applications.

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
