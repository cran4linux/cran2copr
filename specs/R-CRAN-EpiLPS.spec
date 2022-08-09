%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EpiLPS
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          A Bayesian Tool for Fast and Flexible Estimation of the Reproduction Number

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-MASS >= 7.3.54
BuildRequires:    R-grDevices >= 4.1.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-EpiEstim >= 2.2.4
BuildRequires:    R-CRAN-crayon >= 1.4.1
BuildRequires:    R-CRAN-progress >= 1.2.2
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-coda >= 0.19.4
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-MASS >= 7.3.54
Requires:         R-grDevices >= 4.1.0
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-EpiEstim >= 2.2.4
Requires:         R-CRAN-crayon >= 1.4.1
Requires:         R-CRAN-progress >= 1.2.2
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-coda >= 0.19.4

%description
Estimation of the instantaneous reproduction number with
Laplacian-P-splines following the methodology of Gressani et al.(2021)
<doi:10.1101/2021.12.02.21267189>. The negative Binomial distribution is
used to model the time series of case counts. Two methods are available
for inference : (1) a sampling-free approach based on a maximum a
posteriori calibration of the hyperparameter vector and (2) a fully
stochastic approach with a Metropolis-within-Gibbs algorithm and Langevin
diffusions for efficient sampling of the posterior distribution.

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
