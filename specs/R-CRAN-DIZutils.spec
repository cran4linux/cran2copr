%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DIZutils
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Utilities for 'DIZ' R Package Development

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DBI >= 1.1.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-DIZtools 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-RJDBC 
BuildRequires:    R-CRAN-RJSONIO 
BuildRequires:    R-CRAN-RPostgres 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-DBI >= 1.1.0
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-DIZtools 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-RJDBC 
Requires:         R-CRAN-RJSONIO 
Requires:         R-CRAN-RPostgres 
Requires:         R-CRAN-xml2 

%description
Utility functions used for the R package development infrastructure inside
the data integration centers ('DIZ') to standardize and facilitate
repetitive tasks such as setting up a database connection or issuing
notification messages and to avoid redundancy.

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
