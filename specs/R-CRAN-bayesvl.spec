%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bayesvl
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Visually Learning the Graphical Structure of Bayesian Networks and Performing MCMC with 'Stan'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-rstan >= 2.10.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-bnlearn 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-bayesplot 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-StanHeaders >= 2.18.0
Requires:         R-CRAN-rstan >= 2.10.0
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-bnlearn 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-bayesplot 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rstantools

%description
Provides users with its associated functions for pedagogical purposes in
visually learning Bayesian networks and Markov chain Monte Carlo (MCMC)
computations. It enables users to: a) Create and examine the (starting)
graphical structure of Bayesian networks; b) Create random Bayesian
networks using a dataset with customized constraints; c) Generate Stan
code for structures of Bayesian networks for sampling the data and
learning parameters; d) Plot the network graphs; e) Perform Markov chain
Monte Carlo computations and produce graphs for posteriors checks. The
package refers to one reference item, which describes the methods and
algorithms: Vuong, Quan-Hoang and La, Viet-Phuong (2019)
<doi:10.31219/osf.io/w5dx6> The 'bayesvl' R package. Open Science
Framework (May 18).

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
