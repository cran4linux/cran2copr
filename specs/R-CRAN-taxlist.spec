%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  taxlist
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Handling Taxonomic Lists

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3
Requires:         R-core >= 4.3
BuildArch:        noarch
BuildRequires:    R-CRAN-biblio >= 0.0.8
BuildRequires:    R-CRAN-foreign 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vegdata 
Requires:         R-CRAN-biblio >= 0.0.8
Requires:         R-CRAN-foreign 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringr 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-vegdata 

%description
Handling taxonomic lists through objects of class 'taxlist'. This package
provides functions to import species lists from 'Turboveg'
(<https://www.synbiosys.alterra.nl/turboveg/>) and the possibility to
create backups from resulting R-objects. Also quick displays are
implemented as summary-methods.

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
