%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  irace
%global packver   4.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Iterated Racing for Automatic Algorithm Configuration

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-matrixStats >= 1.4.1
BuildRequires:    R-CRAN-data.table >= 1.15.0
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-codetools 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-spacefillr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-matrixStats >= 1.4.1
Requires:         R-CRAN-data.table >= 1.15.0
Requires:         R-CRAN-R6 
Requires:         R-CRAN-codetools 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-spacefillr 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
Iterated race is an extension of the Iterated F-race method for the
automatic configuration of optimization algorithms, that is, (offline)
tuning their parameters by finding the most appropriate settings given a
set of instances of an optimization problem. M. López-Ibáñez, J.
Dubois-Lacoste, L. Pérez Cáceres, T. Stützle, and M. Birattari (2016)
<doi:10.1016/j.orp.2016.09.002>.

%prep
%setup -q -c -n %{packname}
find %{packname} -type f -exec sed -Ei 's@#!( )*(/usr)*/bin/(env )*python@#!/usr/bin/python3@g' {} \;
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
