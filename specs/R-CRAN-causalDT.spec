%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  causalDT
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Causal Distillation Trees

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-bcf 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggparty 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-grf 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-bcf 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggparty 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-grf 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-partykit 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyselect 

%description
Causal Distillation Tree (CDT) is a novel machine learning method for
estimating interpretable subgroups with heterogeneous treatment effects.
CDT allows researchers to fit any machine learning model (or metalearner)
to estimate heterogeneous treatment effects for each individual, and then
"distills" these predicted heterogeneous treatment effects into
interpretable subgroups by fitting an ordinary decision tree to predict
the previously-estimated heterogeneous treatment effects. This package
provides tools to estimate causal distillation trees (CDT), as detailed in
Huang, Tang, and Kenney (2025) <doi:10.48550/arXiv.2502.07275>.

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
