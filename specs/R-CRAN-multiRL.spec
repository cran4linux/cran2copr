%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  multiRL
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Reinforcement Learning Tools for Multi-Armed Bandit

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-grDevices 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-future 
Requires:         R-CRAN-doFuture 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-grDevices 

%description
A flexible general-purpose toolbox for implementing Rescorla-Wagner models
in multi-armed bandit tasks. As the successor and functional extension of
the 'binaryRL' package, 'multiRL' modularizes the Markov Decision Process
(MDP) into six core components. This framework enables users to construct
custom models via intuitive if-else syntax and define latent learning
rules for agents. For parameter estimation, it provides both
likelihood-based inference (MLE and MAP) and simulation-based inference
(ABC and RNN), with full support for parallel processing across subjects.
The workflow is highly standardized, featuring four main functions that
strictly follow the four-step protocol (and ten rules) proposed by Wilson
& Collins (2019) <doi:10.7554/eLife.49547>. Beyond the three built-in
models (TD, RSTD, and Utility), users can easily derive new variants by
declaring which variables are treated as free parameters.

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
