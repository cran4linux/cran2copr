%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DiscreteDLM
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Distributed Lag Model Fitting for Binary and Count Response Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-BayesLogit 
BuildRequires:    R-CRAN-dlnm 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-BayesLogit 
Requires:         R-CRAN-dlnm 
Requires:         R-splines 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-reshape2 

%description
Tools for fitting Bayesian Distributed Lag Models (DLMs) to longitudinal
response data that is a count or binary. Count data is fit using negative
binomial regression and binary is fit using quantile regression. The
contribution of the lags are fit via b-splines. In addition, infers the
predictor inclusion uncertainty. Multimomial models are not supported.
Based on Dempsey and Wyse (2025) <doi:10.48550/arXiv.2403.03646>.

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
