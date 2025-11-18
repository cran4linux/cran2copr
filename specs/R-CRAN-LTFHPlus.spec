%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LTFHPlus
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Implementation of LT-FH++

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-batchmeans 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-batchmeans 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-future 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 

%description
Implementation of LT-FH++, an extension of the liability threshold family
history (LT-FH) model. LT-FH++ uses a Gibbs sampler for sampling from the
truncated multivariate normal distribution and allows for flexible family
structures. LT-FH++ was first described in Pedersen, Emil M., et al.
(2022) <doi:10.1016/j.ajhg.2022.01.009> as an extension to LT-FH with more
flexible family structures, and again as the age-dependent liability
threshold (ADuLT) model Pedersen, Emil M., et al. (2023)
<https://www.nature.com/articles/s41467-023-41210-z> as an alternative to
traditional time-to-event genome-wide association studies, where family
history was not considered.

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
