%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MECfda
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Scalar-on-Function Regression with Measurement Error Correction

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-gss 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-glme 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-refund 
BuildRequires:    R-CRAN-pracma 
Requires:         R-stats 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-quantreg 
Requires:         R-splines 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-gss 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-glme 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-refund 
Requires:         R-CRAN-pracma 

%description
Solve scalar-on-function linear models, including generalized linear mixed
effect model and quantile linear regression model, and bias correction
estimation methods due to measurement error. Details about the measurement
error bias correction methods, see Luan et al. (2023)
<doi:10.48550/arXiv.2305.12624>, Tekwe et al. (2022)
<doi:10.1093/biostatistics/kxac017>, Zhang et al. (2023)
<doi:10.5705/ss.202021.0246>, Tekwe et al. (2019) <doi:10.1002/sim.8179>.

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
