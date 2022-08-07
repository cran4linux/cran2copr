%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nflreadr
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Download 'nflverse' Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 4.3.0
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-CRAN-memoise >= 2.0.0
BuildRequires:    R-CRAN-glue >= 1.4.0
BuildRequires:    R-CRAN-data.table >= 1.14.0
BuildRequires:    R-CRAN-cachem >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.4.10
BuildRequires:    R-CRAN-rappdirs >= 0.3.0
BuildRequires:    R-methods 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-curl >= 4.3.0
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-memoise >= 2.0.0
Requires:         R-CRAN-glue >= 1.4.0
Requires:         R-CRAN-data.table >= 1.14.0
Requires:         R-CRAN-cachem >= 1.0.0
Requires:         R-CRAN-rlang >= 0.4.10
Requires:         R-CRAN-rappdirs >= 0.3.0
Requires:         R-methods 
Requires:         R-tools 
Requires:         R-utils 

%description
A minimal package for downloading data from 'GitHub' repositories of the
'nflverse' project.

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
