%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  animint2
%global packver   2025.9.16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2025.9.16
Release:          1%{?dist}%{?buildtag}
Summary:          Animated Interactive Grammar of Graphics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.9.8
BuildRequires:    R-CRAN-plyr >= 1.7.1
BuildRequires:    R-CRAN-knitr >= 1.5
BuildRequires:    R-CRAN-scales >= 0.4.1
BuildRequires:    R-CRAN-gtable >= 0.1.1
BuildRequires:    R-CRAN-servr 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-RJSONIO 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-data.table >= 1.9.8
Requires:         R-CRAN-plyr >= 1.7.1
Requires:         R-CRAN-knitr >= 1.5
Requires:         R-CRAN-scales >= 0.4.1
Requires:         R-CRAN-gtable >= 0.1.1
Requires:         R-CRAN-servr 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-RJSONIO 
Requires:         R-grid 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-methods 

%description
Functions are provided for defining animated, interactive data
visualizations in R code, and rendering on a web page. The 2018 Journal of
Computational and Graphical Statistics paper,
<doi:10.1080/10618600.2018.1513367> describes the concepts implemented.

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
