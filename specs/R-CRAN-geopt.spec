%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geopt
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools to Access and Map Spatial Datasets of Portugal

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-geojsonsf 
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-CRAN-R6 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-geojsonsf 
Requires:         R-CRAN-digest 

%description
Tools to download, process, and visualize official spatial datasets for
Portugal. Get administrative boundaries at all levels and other geographic
data ready for mapping. Data from Statistics Portugal (INE), for example
retrieved with the 'ineptr2' package, can be joined to the boundaries by
place name or code, including names from earlier boundary reforms.

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
