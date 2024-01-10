%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  when
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Definition of Date and Time Dimension Tables

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-dm 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-hms 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-snakecase 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xlsx 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-dm 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-hms 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-snakecase 
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-xlsx 

%description
In Multidimensional Systems the When dimension allows us to express when
the analysed facts have occurred. The purpose of this package is to
provide support for implementing this dimension in the form of date and
time tables for Relational On-Line Analytical Processing star database
systems.

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
