%global __brp_check_rpaths %{nil}
%global packname  eks
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tidy and Geospatial Kernel Smoothing

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-isoband 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-mapsf 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-isoband 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-mapsf 
Requires:         R-CRAN-sf 

%description
Extensions of the kernel smoothing functions from the 'ks' package for
compatibility with the tidyverse and geospatial ecosystems.

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
