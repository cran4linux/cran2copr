%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ZIDW
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Zero-Inflated Discrete Weibull Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DWreg 
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-COUNT 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-DiscreteWeibull 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-DWreg 
Requires:         R-CRAN-actuar 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-COUNT 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-DiscreteWeibull 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 

%description
Parameter estimation for zero-inflated discrete Weibull (ZIDW) regression
models, the univariate setting, distribution functions, functions to
generate randomized quantile residuals a pseudo R2, and plotting of
rootograms. For more details, see Kalktawi (2017)
<https://bura.brunel.ac.uk/handle/2438/14476>, Taconeli and Rodrigues de
Lara (2022) <doi:10.1080/00949655.2021.2005597>, and Yeh and Young (2025)
<doi:10.1080/03610918.2025.2464076>.

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
