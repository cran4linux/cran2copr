%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sandwichr
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Interpolation Based on Spatial Stratified Heterogeneity

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-geodetector 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-lwgeom 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-geodetector 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-lwgeom 
Requires:         R-tools 
Requires:         R-CRAN-dplyr 

%description
Spatial interpolation is a common practice in social and environmental
science. This package enables the implementation of SSH-based spatial
interpolation proposed by Wang et al. (2013) <doi:10.1068/a44710>. It
provides functions to (1) evaluate stratification schemes, (2) interpolate
sampling data over user-defined reporting units, (3) assess interpolation
uncertainties, and (4) evaluate overall accuracy using the k-fold
cross-validation estimate.

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
