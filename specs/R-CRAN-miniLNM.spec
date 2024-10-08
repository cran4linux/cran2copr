%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  miniLNM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Miniature Logistic-Normal Multinomial Models

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-rstantools >= 2.4.0
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fansi 
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-posterior 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-rstantools >= 2.4.0
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fansi 
Requires:         R-CRAN-formula.tools 
Requires:         R-CRAN-glue 
Requires:         R-methods 
Requires:         R-CRAN-posterior 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-rstantools

%description
Logistic-normal Multinomial (LNM) models are common in problems with
multivariate count data. This package gives a simple implementation with a
30 line 'Stan' script. This lightweight implementation makes it an easy
starting point for other projects, in particular for downstream tasks that
require analysis of "compositional" data. It can be applied whenever a
multinomial probability parameter is thought to depend linearly on inputs
in a transformed, log ratio space. Additional utilities make it easy to
inspect, create predictions, and draw samples using the fitted models.
More about the LNM can be found in Xia et al. (2013) "A Logistic Normal
Multinomial Regression Model for Microbiome Compositional Data Analysis"
<doi:10.1111/biom.12079> and Sankaran and Holmes (2023) "Generative
Models: An Interdisciplinary Perspective"
<doi:10.1146/annurev-statistics-033121-110134>.

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
