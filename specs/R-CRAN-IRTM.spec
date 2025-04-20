%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  IRTM
%global packver   0.0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Theory-Driven Item Response Theory (IRT) Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-RcppDist 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-utils 
Requires:         R-CRAN-RcppProgress 
Requires:         R-CRAN-RcppDist 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-reshape2 

%description
IRT-M is a semi-supervised approach based on Bayesian Item Response Theory
that produces theoretically identified underlying dimensions from input
data and a constraints matrix. The methodology is fully described in
'Morucci et al. (2024), "Measurement That Matches Theory: Theory-Driven
Identification in Item Response Theory Models"'. Details are available at
<https://www.cambridge.org/core/journals/american-political-science-review/article/measurement-that-matches-theory-theorydriven-identification-in-item-response-theory-models/395DA1DFE3DCD7B866DC053D7554A30B>.

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
