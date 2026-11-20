%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  multiScaleR
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate Scales of Effect for Spatial Ecological Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3
Requires:         R-core >= 4.3
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-insight 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-unmarked 
BuildRequires:    R-CRAN-exactextractr 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-optimParallel 
BuildRequires:    R-CRAN-AICcmodavg 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-insight 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-tools 
Requires:         R-CRAN-unmarked 
Requires:         R-CRAN-exactextractr 
Requires:         R-CRAN-crayon 
Requires:         R-parallel 
Requires:         R-CRAN-optimParallel 
Requires:         R-CRAN-AICcmodavg 
Requires:         R-methods 
Requires:         R-CRAN-sf 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Estimates the scale of effect, the distance over which a landscape
variable influences an ecological response. Raster values around each
sample location are weighted with a distance kernel, and the kernel scale
that maximizes the likelihood of a fitted regression model is found. Works
with linear, generalized linear, additive, and mixed models, with
'unmarked' occupancy, abundance, and distance-removal models, and with
step-selection models, and fits Bayesian models in which scales vary among
years or with covariates. Also provides kernel-weighted landscape and
surface metrics, cross-validation, model selection tables, fast kernel
smoothing of rasters for mapping predictions, and simulation of data with
known scales of effect. For more details see Peterman (2026)
<doi:10.1007/s10980-025-02267-x>.

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
