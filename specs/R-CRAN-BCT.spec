%global __brp_check_rpaths %{nil}
%global packname  BCT
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Context Trees for Discrete Time Series

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-igraph 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
An implementation of a collection of tools for exact Bayesian inference
with discrete times series. This package contains functions that can be
used for prediction, model selection, estimation,
segmentation/change-point detection and other statistical tasks.
Specifically, the functions provided can be used for the exact computation
of the prior predictive likelihood of the data, for the identification of
the a posteriori most likely (MAP) variable-memory Markov models, for
calculating the exact posterior probabilities and the AIC and BIC scores
of these models, for prediction with respect to log-loss and 0-1 loss and
segmentation/change-point detection. Example data sets from finance,
genetics, animal communication and meteorology are also provided. Detailed
descriptions of the underlying theory and algorithms can be found in
[Kontoyiannis et al. 'Bayesian Context Trees: Modelling and exact
inference for discrete time series.' Journal of the Royal Statistical
Society: Series B (Statistical Methodology), April 2022. Available at:
<arXiv:2007.14900> [stat.ME], July 2020] and [Lungu et al. 'Change-point
Detection and Segmentation of Discrete Data using Bayesian Context Trees'
<arXiv:2203.04341> [stat.ME], March 2022].

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
