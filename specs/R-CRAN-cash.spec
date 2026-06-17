%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cash
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Discrete Choice and Competitive Reactions: End-to-End Simulation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-idefix >= 1.1.0
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-DoE.base 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-bayesm 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-arrangements 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-idefix >= 1.1.0
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-DoE.base 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-bayesm 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-arrangements 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 

%description
Although discrete choice (choice-based conjoint) analysis has become a
widely used technique for the elicitation of consumer preferences and
hence a foundation for product design, to the best of our knowledge, there
exists neither free and open-source nor commercial software that covers
the game-theoretic simulation of competitive reactions among firms based
on discrete choice models to improve decision making beyond traditional
product (line) optimization. The package does not only provide functions
to fill this gap but comprises an entire simulation pipeline including the
upstream processes of discrete choice analysis itself. It ranges from
preference generation, choice design, design assessment, error and
response simulation, through hierarchical Bayesian estimation of mixed
logit models as well as convergence and model assessment, to Nash
equilibrium computation. Doing so, it partly draws from established
packages concerned with discrete choice analysis. While its structure
generally aims towards end-to-end simulation as well as simulation of
competitive dynamics based on real data, all its key elements mentioned
above may be of use independently of each other. For implementation and
application details, see Dressler et al. (2026)
<doi:10.48550/arXiv.2606.15593>.

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
