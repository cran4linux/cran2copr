%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  STCCGEV
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Conditional Copula Model for Crop Yield Forecasting

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bsts 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-bsts 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-rootSolve 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides functions to model and forecast crop yields using a spatial
temporal conditional copula approach. The package incorporates extreme
weather covariates and Bayesian Structural Time Series models to analyze
crop yield dependencies across multiple regions. Includes tools for
fitting, simulating, and visualizing results. This method build upon
established R packages, including 'Hofert' 'et' 'al'. (2025)
<doi:10.32614/CRAN.package.copula>, 'Scott' (2024)
<doi:10.32614/CRAN.package.bsts>, and 'Stephenson' 'et' 'al'. (2024)
<doi:10.32614/CRAN.package.evd>.

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
