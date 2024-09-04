%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lnmixsurv
%global packver   3.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Mixture Log-Normal Survival Model

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-hardhat >= 1.3.0
BuildRequires:    R-CRAN-parsnip >= 1.1.0
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-posterior 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppGSL 
Requires:         R-CRAN-hardhat >= 1.3.0
Requires:         R-CRAN-parsnip >= 1.1.0
Requires:         R-CRAN-survival 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-posterior 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-broom 

%description
Bayesian Survival models via the mixture of Log-Normal distribution
extends the well-known survival models and accommodates different
behaviour over time and considers higher censored survival times. The
proposal combines mixture distributions Fruhwirth-Schnatter(2006)
<doi:10.1007/s11336-009-9121-4>, and data augmentation techniques Tanner
and Wong (1987) <doi:10.1080/01621459.1987.10478458>.

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
