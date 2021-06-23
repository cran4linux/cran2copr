%global __brp_check_rpaths %{nil}
%global packname  briskaR
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Biological Risk Assessment

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-MASS >= 7.3.29
BuildRequires:    R-stats >= 3.0.2
BuildRequires:    R-grDevices >= 3.0.0
BuildRequires:    R-graphics >= 3.0.0
BuildRequires:    R-CRAN-testthat >= 3.0.0
BuildRequires:    R-CRAN-raster >= 2.3.0
BuildRequires:    R-CRAN-mvtnorm >= 1.0.2
BuildRequires:    R-CRAN-sp >= 1.0.17
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-fftwtools >= 0.9.6
BuildRequires:    R-CRAN-rgdal >= 0.9
BuildRequires:    R-CRAN-sf >= 0.7.1
BuildRequires:    R-CRAN-rgeos >= 0.3
BuildRequires:    R-CRAN-deldir >= 0.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-fasterize 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-MASS >= 7.3.29
Requires:         R-stats >= 3.0.2
Requires:         R-grDevices >= 3.0.0
Requires:         R-graphics >= 3.0.0
Requires:         R-CRAN-raster >= 2.3.0
Requires:         R-CRAN-mvtnorm >= 1.0.2
Requires:         R-CRAN-sp >= 1.0.17
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-fftwtools >= 0.9.6
Requires:         R-CRAN-rgdal >= 0.9
Requires:         R-CRAN-sf >= 0.7.1
Requires:         R-CRAN-rgeos >= 0.3
Requires:         R-CRAN-deldir >= 0.1
Requires:         R-methods 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-fasterize 

%description
A spatio-temporal exposure-hazard model for assessing biological risk and
impact. The model is based on stochastic geometry for describing the
landscape and the exposed individuals, a dispersal kernel for the
dissemination of contaminants, a set of tools to handle spatio-temporal
dataframe and ecotoxicological equations. Walker E, Leclerc M, Rey JF,
Beaudouin R, Soubeyrand S, and Messean A, (2017), A Spatio-Temporal
Exposure-Hazard Model for Assessing Biological Risk and Impact, Risk
Analysis, <doi:10.1111/risa.12941>. Leclerc M, Walker E, Messean A,
Soubeyrand S (2018), Spatial exposure-hazard and landscape models for
assessing the impact of GM crops on non-target organisms, Science of the
Total Environment, 624, 470-479.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
