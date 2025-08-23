%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  redlist
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to the IUCN Red List Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.3
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-httr2 >= 1.1.2
BuildRequires:    R-CRAN-rvest >= 1.0.4
BuildRequires:    R-methods 
Requires:         R-CRAN-cli >= 3.6.3
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-httr2 >= 1.1.2
Requires:         R-CRAN-rvest >= 1.0.4
Requires:         R-methods 

%description
Provides an interface to access data from the International Union for
Conservation of Nature (IUCN) Red List
<https://api.iucnredlist.org/api-docs/index.html>. It allows users to
retrieve up-to-date information on species' conservation status,
supporting biodiversity research and conservation efforts.

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
