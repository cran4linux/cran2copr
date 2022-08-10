%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dispRity
%global packver   1.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Measuring Disparity

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-castor 
BuildRequires:    R-CRAN-Claddis 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-phyclust 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-ape 
Requires:         R-stats 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-castor 
Requires:         R-CRAN-Claddis 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-geometry 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-mnormt 
Requires:         R-parallel 
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-phyclust 
Requires:         R-utils 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-scales 

%description
A modular package for measuring disparity (multidimensional space
occupancy). Disparity can be calculated from any matrix defining a
multidimensional space. The package provides a set of implemented metrics
to measure properties of the space and allows users to provide and test
their own metrics. The package also provides functions for looking at
disparity in a serial way (e.g. disparity through time) or per groups as
well as visualising the results. Finally, this package provides several
statistical tests for disparity analysis.

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
