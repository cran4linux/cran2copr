%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  move
%global packver   4.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Visualizing and Analyzing Animal Track Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-raster >= 3.6.14
BuildRequires:    R-CRAN-geosphere >= 1.4.3
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-raster >= 3.6.14
Requires:         R-CRAN-geosphere >= 1.4.3
Requires:         R-methods 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-Rcpp 

%description
Contains functions to access movement data stored in 'movebank.org' as
well as tools to visualize and statistically analyze animal movement data,
among others functions to calculate dynamic Brownian Bridge Movement
Models. Move helps addressing movement ecology questions.

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
