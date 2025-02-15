%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rKIN
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          (Kernel) Isotope Niche Estimation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-randomcoloR 
BuildRequires:    R-CRAN-shades 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-randomcoloR 
Requires:         R-CRAN-shades 
Requires:         R-CRAN-dplyr 

%description
Applies methods used to estimate animal homerange, but instead of
geospatial coordinates, we use isotopic coordinates. The estimation
methods include: 1) 2-dimensional bivariate normal kernel utilization
density estimator, 2) bivariate normal ellipse estimator, and 3) minimum
convex polygon estimator, all applied to stable isotope data.
Additionally, functions to determine niche area, polygon overlap between
groups and levels (confidence contours) and plotting capabilities.

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
