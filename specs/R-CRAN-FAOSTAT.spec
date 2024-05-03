%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FAOSTAT
%global packver   2.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Download Data from the FAOSTAT Database

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.22
BuildRequires:    R-CRAN-data.table >= 1.8.2
BuildRequires:    R-CRAN-plyr >= 1.7.1
BuildRequires:    R-CRAN-httr >= 1.0
BuildRequires:    R-CRAN-RJSONIO >= 0.96.0
BuildRequires:    R-CRAN-classInt >= 0.1.19
BuildRequires:    R-CRAN-labeling >= 0.1
Requires:         R-CRAN-MASS >= 7.3.22
Requires:         R-CRAN-data.table >= 1.8.2
Requires:         R-CRAN-plyr >= 1.7.1
Requires:         R-CRAN-httr >= 1.0
Requires:         R-CRAN-RJSONIO >= 0.96.0
Requires:         R-CRAN-classInt >= 0.1.19
Requires:         R-CRAN-labeling >= 0.1

%description
Download Data from the FAOSTAT Database of the Food and Agricultural
Organization (FAO) of the United Nations. A list of functions to download
statistics from FAOSTAT (database of the FAO
<https://www.fao.org/faostat/>) and WDI (database of the World Bank
<https://data.worldbank.org/>), and to perform some harmonization
operations.

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
