%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gpss
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Gaussian Processes for Social Science

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.14
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.14
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 

%description
Provides Gaussian process (GP) regression tools for social science
inference problems.  GPs combine flexible nonparametric regression with
principled uncertainty quantification: rather than committing to a single
model fit, the posterior reflects lesser knowledge at the edge of or
beyond the observed data, where other approaches become highly
model-dependent.  The package reduces user-chosen hyperparameters from
three to zero and supplies convenience functions for regression
discontinuity (gp_rdd()), interrupted time-series (gp_its()), and general
GP fitting (gpss(), gp_train(), gp_predict()).  Methods are described in
Cho, Kim, and Hazlett (2026) <doi:10.1017/pan.2026.10032>.

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
