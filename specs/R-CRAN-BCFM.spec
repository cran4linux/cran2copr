%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BCFM
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Clustering Factor Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fastmatrix 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppArmadillo 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fastmatrix 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-tibble 

%description
Implements the Bayesian Clustering Factor Models (BCFM) for simultaneous
clustering and latent factor analysis of multivariate longitudinal data.
The model accounts for within-cluster dependence through shared latent
factors while allowing heterogeneity across clusters, enabling flexible
covariance modeling in high-dimensional settings. Inference is performed
using Markov chain Monte Carlo (MCMC) methods with computationally
intensive steps implemented via 'Rcpp'. Model selection and visualization
tools are provided. The methodology is described in Shin, Ferreira, and
Tegge (2018) <doi:10.1002/sim.70350>.

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
