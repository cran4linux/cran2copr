%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  texmex
%global packver   2.4.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.9
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Modelling of Extreme Values

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 0.12.18
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 

%description
Statistical extreme value modelling of threshold excesses, maxima and
multivariate extremes. Univariate models for threshold excesses and maxima
are the Generalised Pareto, and Generalised Extreme Value model
respectively. These models may be fitted by using maximum (optionally
penalised-)likelihood, or Bayesian estimation, and both classes of models
may be fitted with covariates in any/all model parameters. Model
diagnostics support the fitting process. Graphical output for visualising
fitted models and return level estimates is provided. For serially
dependent sequences, the intervals declustering algorithm of Ferro and
Segers (2003) <doi:10.1111/1467-9868.00401> is provided, with diagnostic
support to aid selection of threshold and declustering horizon.
Multivariate modelling is performed via the conditional approach of
Heffernan and Tawn (2004) <doi:10.1111/j.1467-9868.2004.02050.x>, with
graphical tools for threshold selection and to diagnose estimation
convergence.

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
