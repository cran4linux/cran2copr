%global packname  oxcovid19
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          An R API to the Oxford COVID-19 Database

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-RPostgres 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-dbplyr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-countrycode 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-RPostgres 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-dbplyr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-countrycode 
Requires:         R-CRAN-magrittr 

%description
The OxCOVID19 Project <https://covid19.eng.ox.ac.uk> aims to increase our
understanding of the COVID-19 pandemic and elaborate possible strategies
to reduce the impact on the society through the combined power of
statistical, mathematical modelling, and machine learning techniques. The
OxCOVID19 Database is a large, single-centre, multimodal relational
database consisting of information (using acknowledged sources) related to
COVID-19 pandemic. This package provides an R-specific interface to the
OxCOVID19 Database based on widely-used data handling and manipulation
approaches in R.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
