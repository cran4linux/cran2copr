%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  florabr
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Explore Brazilian Flora 2020 Database

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats >= 4.2.3
BuildRequires:    R-utils >= 4.2.3
BuildRequires:    R-grDevices >= 4.2.3
BuildRequires:    R-CRAN-XML >= 3.99.0.14
BuildRequires:    R-CRAN-terra >= 1.7.39
BuildRequires:    R-CRAN-httr >= 1.4.6
BuildRequires:    R-CRAN-data.table >= 1.14.8
Requires:         R-stats >= 4.2.3
Requires:         R-utils >= 4.2.3
Requires:         R-grDevices >= 4.2.3
Requires:         R-CRAN-XML >= 3.99.0.14
Requires:         R-CRAN-terra >= 1.7.39
Requires:         R-CRAN-httr >= 1.4.6
Requires:         R-CRAN-data.table >= 1.14.8

%description
A collection of functions designed to retrieve, filter and spatialize data
from the Brazilian Flora 2020 dataset. For more information about the
dataset, please visit <https://floradobrasil.jbrj.gov.br/consulta/>.

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
