%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rACMEMEEV
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Variate Measurement Error Adjustment

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-bayesplot 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-snow 
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-rjags 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rstan 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-bayesplot 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-snow 
Requires:         R-CRAN-parallelly 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rstantools

%description
A methodology to perform multivariate measurement error adjustment using
external validation data. Allows users to remove the attenuating effect of
measurement error by incorporating a distribution of external validation
data, and allows for plotting of all resultant adjustments. Sensitivity
analyses can also be run through this package to test how different ranges
of validity coefficients can impact the effect of the measurement error
adjustment. The methods implemented in this package are based on the work
by Muoka, A., Agogo, G., Ngesa, O., Mwambi, H. (2020):
<doi:10.12688/f1000research.27892.1>.

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
