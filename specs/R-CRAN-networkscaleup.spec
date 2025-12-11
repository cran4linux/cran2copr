%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  networkscaleup
%global packver   0.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Network Scale-Up Models for Aggregated Relational Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-rstan >= 2.26.0
BuildRequires:    R-CRAN-StanHeaders >= 2.26.0
BuildRequires:    R-CRAN-LaplacesDemon >= 16.1.6
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-glmmTMB 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-trialr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-RMTstat 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-rstan >= 2.26.0
Requires:         R-CRAN-LaplacesDemon >= 16.1.6
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-graphics 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-glmmTMB 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-trialr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-RMTstat 
Requires:         R-CRAN-rstantools

%description
Provides a variety of Network Scale-up Models for researchers to analyze
Aggregated Relational Data, through the use of Stan and 'glmmTMB'. Also
provides tools for model checking In this version, the package implements
models from Laga, I., Bao, L., and Niu, X (2023)
<doi:10.1080/01621459.2023.2165929>, Zheng, T., Salganik, M. J., and
Gelman, A. (2006) <doi:10.1198/016214505000001168>, Killworth, P. D.,
Johnsen, E. C., McCarty, C., Shelley, G. A., and Bernard, H. R. (1998)
<doi:10.1016/S0378-8733(96)00305-X>, and Killworth, P. D., McCarty, C.,
Bernard, H. R., Shelley, G. A., and Johnsen, E. C. (1998)
<doi:10.1177/0193841X9802200205>.

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
