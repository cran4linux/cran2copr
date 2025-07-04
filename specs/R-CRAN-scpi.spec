%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  scpi
%global packver   3.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Prediction Intervals for Synthetic Control Methods with Multiple Treated Units and Staggered Adoption

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3
BuildRequires:    R-utils >= 4.1.1
BuildRequires:    R-methods >= 4.1.0
BuildRequires:    R-parallel >= 4.1.0
BuildRequires:    R-stats >= 4.1.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.3
BuildRequires:    R-CRAN-tibble >= 3.1.2
BuildRequires:    R-CRAN-Rdpack >= 2.4
BuildRequires:    R-CRAN-magrittr >= 2.0.1
BuildRequires:    R-CRAN-fastDummies >= 1.6.3
BuildRequires:    R-CRAN-Qtools >= 1.5.6
BuildRequires:    R-CRAN-foreach >= 1.5.1
BuildRequires:    R-CRAN-abind >= 1.4.5
BuildRequires:    R-CRAN-reshape2 >= 1.4.4
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-Matrix >= 1.3.3
BuildRequires:    R-CRAN-tidyr >= 1.1.3
BuildRequires:    R-CRAN-dplyr >= 1.0.7
BuildRequires:    R-CRAN-doSNOW >= 1.0.19
BuildRequires:    R-CRAN-CVXR >= 1.0.10
BuildRequires:    R-CRAN-ECOSolveR >= 0.5.4
BuildRequires:    R-CRAN-rlang >= 0.4.11
BuildRequires:    R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-MASS >= 7.3
Requires:         R-utils >= 4.1.1
Requires:         R-methods >= 4.1.0
Requires:         R-parallel >= 4.1.0
Requires:         R-stats >= 4.1.0
Requires:         R-CRAN-ggplot2 >= 3.3.3
Requires:         R-CRAN-tibble >= 3.1.2
Requires:         R-CRAN-Rdpack >= 2.4
Requires:         R-CRAN-magrittr >= 2.0.1
Requires:         R-CRAN-fastDummies >= 1.6.3
Requires:         R-CRAN-Qtools >= 1.5.6
Requires:         R-CRAN-foreach >= 1.5.1
Requires:         R-CRAN-abind >= 1.4.5
Requires:         R-CRAN-reshape2 >= 1.4.4
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-Matrix >= 1.3.3
Requires:         R-CRAN-tidyr >= 1.1.3
Requires:         R-CRAN-dplyr >= 1.0.7
Requires:         R-CRAN-doSNOW >= 1.0.19
Requires:         R-CRAN-CVXR >= 1.0.10
Requires:         R-CRAN-ECOSolveR >= 0.5.4
Requires:         R-CRAN-rlang >= 0.4.11
Requires:         R-CRAN-purrr >= 0.3.4

%description
Implementation of prediction and inference procedures for Synthetic
Control methods using least square, lasso, ridge, or simplex-type
constraints. Uncertainty is quantified with prediction intervals as
developed in Cattaneo, Feng, and Titiunik (2021)
<doi:10.1080/01621459.2021.1979561> for a single treated unit and in
Cattaneo, Feng, Palomba, and Titiunik (2025) <doi:10.1162/rest_a_01588>
for multiple treated units and staggered adoption. More details about the
software implementation can be found in Cattaneo, Feng, Palomba, and
Titiunik (2025) <doi:10.18637/jss.v113.i01>.

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
