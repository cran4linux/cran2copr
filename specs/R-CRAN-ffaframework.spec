%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ffaframework
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Flood Frequency Analysis Framework

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-base64enc 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-httr 
Requires:         R-stats 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-base64enc 

%description
Tools to support systematic and reproducible workflows for both stationary
and nonstationary flood frequency analysis, with applications extending to
other hydroclimate extremes, such as precipitation frequency analysis.
This package implements the FFA framework proposed by Vidrio- Sahagún et
al. (2024) <doi:10.1016/j.envsoft.2024.105940>, originally developed in
'MATLAB', now adapted for the 'R' environment. This work was funded by the
Flood Hazard Identification and Mapping Program of Environment and Climate
Change Canada, as well as the Canada Research Chair (Tier 1) awarded to
Dr. Pietroniro.

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
