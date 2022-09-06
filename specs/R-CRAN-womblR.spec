%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  womblR
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Spatiotemporal Boundary Detection Model for Areal Unit Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-msm >= 1.0.0
BuildRequires:    R-CRAN-mvtnorm >= 1.0.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.7.500.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.9
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-msm >= 1.0.0
Requires:         R-CRAN-mvtnorm >= 1.0.0
Requires:         R-CRAN-Rcpp >= 0.12.9
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 

%description
Implements a spatiotemporal boundary detection model with a dissimilarity
metric for areal data with inference in a Bayesian setting using Markov
chain Monte Carlo (MCMC). The response variable can be modeled as Gaussian
(no nugget), probit or Tobit link and spatial correlation is introduced at
each time point through a conditional autoregressive (CAR) prior. Temporal
correlation is introduced through a hierarchical structure and can be
specified as exponential or first-order autoregressive. Full details of
the package can be found in the accompanying vignette. Furthermore, the
details of the package can be found in "Diagnosing Glaucoma Progression
with Visual Field Data Using a Spatiotemporal Boundary Detection Method",
by Berchuck et al (2018), <arXiv:1805.11636>. The paper is in press at the
Journal of the American Statistical Association.

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
