%global __brp_check_rpaths %{nil}
%global packname  africamonitor
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Africa Macroeconomic Monitor Database API

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-RMySQL 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-collapse 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-RMySQL 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-collapse 

%description
An R API providing access to a relational database with macroeconomic data
for Africa. The database contains >700 macroeconomic time series from
mostly international sources, grouped into 50 macroeconomic and
development-related topics. Series are carefully selected on the basis of
data coverage for Africa, frequency, and relevance to the
macro-development context. The project is part of the 'Kiel Institute
Africa Initiative'
<https://www.ifw-kiel.de/institute/initiatives/kielinstituteafricainitiative/>,
which, amongst other things, aims to develop a parsimonious database with
highly relevant indicators to monitor macroeconomic developments in
Africa, accessible through a fast API and a web-based platform at
<https://africamonitor.ifw-kiel.de/>. The database is maintained at the
Kiel Institute for the World Economy <https://www.ifw-kiel.de/>.

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
