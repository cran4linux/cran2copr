%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  clustGLMM
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Model-Based Clustering of Mixed-Type Longitudinal Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-gaussquad 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-HDInterval 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-RcppHungarian 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-gaussquad 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-HDInterval 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-RcppHungarian 
Requires:         R-splines 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides tools for Bayesian estimation and inference for modelling
clusterwise multivariate regression models for numeric, count, binary,
ordinal and count outcomes observed repeatedly on the same units and where
possible relations among outcomes are captured through a joint
distribution of random effects. The clusters are defined through
cluster-specific parameters, which the analyst can choose, e.g., with
respect to the regression coefficients. In particular, the model
specification for each regression model via the formula is specific to the
outcome and consists of four parts: (1) fixed - regression coefficients
common to all clusters, (2) group - group-specific regression
coefficients, (3) random - random effects specific for each unit, (3)
offset - name of an offset variable (if needed). Estimation is performed
using MCMC sampling combining Gibbs and Metropolis-Hastings steps.
Post-processing tools allow to assess convergence and address label
switching and provide visual diagnostics. Units may be classified based on
sampled allocation indicators or by exploiting the posterior distribution
of the classification probabilities. For more details see Vavra et al.
(2024) <doi:10.1007/s11222-023-10304-5>.

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
