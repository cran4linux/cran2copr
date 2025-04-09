%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ctsmTMB
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Continuous Time Stochastic Modelling using Template Model Builder

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-RTMB >= 1.7
BuildRequires:    R-CRAN-TMB 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-Deriv 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-RcppXPtrUtils 
BuildRequires:    R-CRAN-RcppZiggurat 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggfortify 
BuildRequires:    R-CRAN-patchwork 
Requires:         R-CRAN-RTMB >= 1.7
Requires:         R-CRAN-TMB 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-Deriv 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppEigen 
Requires:         R-CRAN-RcppXPtrUtils 
Requires:         R-CRAN-RcppZiggurat 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggfortify 
Requires:         R-CRAN-patchwork 

%description
Perform state and parameter inference, and forecasting, in stochastic
state-space systems using the 'ctsmTMB' class. This class, built with the
'R6' package, provides a user-friendly interface for defining and handling
state-space models. Inference is based on maximum likelihood estimation,
with derivatives efficiently computed through automatic differentiation
enabled by the 'TMB'/'RTMB' packages (Kristensen et al., 2016)
<doi:10.18637/jss.v070.i05>. The available inference methods include
Kalman filters, in addition to a Laplace approximation-based smoothing
method. For further details of these methods refer to the documentation of
the 'CTSMR' package <https://ctsm.info/ctsmr-reference.pdf> and Thygesen
(2025) <doi:10.48550/arXiv.2503.21358>. Forecasting capabilities include
moment predictions and stochastic path simulations, both implemented in
'C++' using 'Rcpp' (Eddelbuettel et al., 2018)
<doi:10.1080/00031305.2017.1375990> for computational efficiency.

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
