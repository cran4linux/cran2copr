%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BCClong
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Consensus Clustering for Multiple Longitudinal Features

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.9
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-label.switching 
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-mixAK 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-Rmpfr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-truncdist 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.9
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-CRAN-label.switching 
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-mixAK 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-Rmpfr 
Requires:         R-stats 
Requires:         R-CRAN-truncdist 

%description
It is very common nowadays for a study to collect multiple features and
appropriately integrating multiple longitudinal features simultaneously
for defining individual clusters becomes increasingly crucial to
understanding population heterogeneity and predicting future outcomes.
'BCClong' implements a Bayesian consensus clustering (BCC) model for
multiple longitudinal features via a generalized linear mixed model.
Compared to existing packages, several key features make the 'BCClong'
package appealing: (a) it allows simultaneous clustering of mixed-type
(e.g., continuous, discrete and categorical) longitudinal features, (b) it
allows each longitudinal feature to be collected from different sources
with measurements taken at distinct sets of time points (known as
irregularly sampled longitudinal data), (c) it relaxes the assumption that
all features have the same clustering structure by estimating the
feature-specific (local) clusterings and consensus (global) clustering.

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
