%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GeoAdjust
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Accounting for Random Displacements of True GPS Coordinates of Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-fmesher 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-SUMMER 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-TMB 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-fmesher 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-CRAN-SUMMER 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-TMB 

%description
The purpose is to account for the random displacements (jittering) of true
survey household cluster center coordinates in geostatistical analyses of
Demographic and Health Surveys program (DHS) data. Adjustment for
jittering can be implemented either in the spatial random effect, or in
the raster/distance based covariates, or in both. Detailed information
about the methods behind the package functionality can be found in our two
papers. Umut Altay, John Paige, Andrea Riebler, Geir-Arne Fuglstad (2024)
<doi:10.32614/RJ-2024-027>. Umut Altay, John Paige, Andrea Riebler,
Geir-Arne Fuglstad (2023) <doi:10.1177/1471082X231219847>.

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
