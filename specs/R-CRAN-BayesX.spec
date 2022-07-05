%global __brp_check_rpaths %{nil}
%global packname  BayesX
%global packver   0.3-1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          R Utilities Accompanying the Software Package BayesX

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shapefiles 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-splines 
BuildRequires:    R-methods 
Requires:         R-CRAN-shapefiles 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-coda 
Requires:         R-splines 
Requires:         R-methods 

%description
Functions for exploring and visualising estimation results obtained with
BayesX, a free software for estimating structured additive regression
models (<http://www.BayesX.org>). In addition, functions that allow to
read, write and manipulate map objects that are required in spatial
analyses performed with BayesX.

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
