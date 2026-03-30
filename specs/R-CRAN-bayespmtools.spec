%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bayespmtools
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Sample Size and Precision Considerations for Risk Prediction Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fastLogisticRegressionWrap 
BuildRequires:    R-CRAN-logitnorm 
BuildRequires:    R-CRAN-mc2d 
BuildRequires:    R-CRAN-mcmapper 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-cobs 
BuildRequires:    R-CRAN-OOR 
BuildRequires:    R-CRAN-quantreg 
Requires:         R-CRAN-fastLogisticRegressionWrap 
Requires:         R-CRAN-logitnorm 
Requires:         R-CRAN-mc2d 
Requires:         R-CRAN-mcmapper 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-cobs 
Requires:         R-CRAN-OOR 
Requires:         R-CRAN-quantreg 

%description
Performs Bayesian sample size, precision, and value-of-information
analysis for external validation of existing multi-variable prediction
models using the approach proposed by Sadatsafavi and colleagues (2025)
<doi:10.1002/sim.70389>.

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
