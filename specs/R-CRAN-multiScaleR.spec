%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  multiScaleR
%global packver   0.4.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.5
Release:          1%{?dist}%{?buildtag}
Summary:          Methods for Optimizing Scales of Effect

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3
Requires:         R-core >= 4.3
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-insight 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-unmarked 
BuildRequires:    R-CRAN-exactextractr 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-optimParallel 
BuildRequires:    R-CRAN-AICcmodavg 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pscl 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-insight 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-unmarked 
Requires:         R-CRAN-exactextractr 
Requires:         R-CRAN-crayon 
Requires:         R-parallel 
Requires:         R-CRAN-optimParallel 
Requires:         R-CRAN-AICcmodavg 
Requires:         R-methods 
Requires:         R-CRAN-pscl 

%description
A tool for optimizing scales of effect when modeling ecological processes
in space. Specifically, the scale parameter of a distance-weighted kernel
distribution is identified for all environmental layers included in the
model. Includes functions to assist in model selection, model evaluation,
efficient transformation of raster surfaces using fast Fourier
transformation, and projecting models. For more details see Peterman
(2025) <doi:10.21203/rs.3.rs-7246115/v1>.

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
