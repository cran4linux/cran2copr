%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MultiscaleDTM
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Scale Geomorphometric Terrain Attributes

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-rgl 
Requires:         R-stats 
Requires:         R-utils 

%description
Calculates multi-scale geomorphometric terrain attributes from regularly
gridded digital terrain models using a variable focal windows size (Misiuk
et al. (2021) <doi:10.1080/01490419.2021.1925789>; Wilson et al. (2007)
<doi:10.1080/01490410701295962>; Wood (1996)
<https://hdl.handle.net/2381/34503>).

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
