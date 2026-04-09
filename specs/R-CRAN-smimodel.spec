%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  smimodel
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Sparse Multiple Index Models for Nonparametric Forecasting

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cgaim 
BuildRequires:    R-CRAN-conformalForecast 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gratia 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-ROI 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tsibble 
BuildRequires:    R-utils 
Requires:         R-CRAN-cgaim 
Requires:         R-CRAN-conformalForecast 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gratia 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-ROI 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tsibble 
Requires:         R-utils 

%description
Implements a general algorithm for estimating Sparse Multiple Index (SMI)
models for nonparametric forecasting and prediction. Estimation of SMI
models requires the Gurobi mixed integer programming (MIP) solver via the
gurobi R package. To use this functionality, the Gurobi Optimizer must be
installed, and a valid license obtained and activated from
<https://www.gurobi.com>. The gurobi R package must then be installed and
configured following the instructions at
<https://support.gurobi.com/hc/en-us/articles/14462206790033-How-do-I-install-Gurobi-for-R>.
The package also includes functions for fitting nonparametric additive
models with backward elimination, group-wise additive index models, and
projection pursuit regression models as benchmark comparison methods. In
addition, it provides tools for generating prediction intervals to
quantify uncertainty in point forecasts produced by the SMI model and
benchmark models, using the classical block bootstrap and a new method
called conformal bootstrap, which integrates block bootstrap with split
conformal prediction.

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
