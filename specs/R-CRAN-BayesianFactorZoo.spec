%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesianFactorZoo
%global packver   0.0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Solutions for the Factor Zoo: We Just Ran Two Quadrillion Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-timeSeries 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-nse 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-timeSeries 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-nse 
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-Matrix 

%description
Contains the functions to use the econometric methods in the paper
Bryzgalova, Huang, and Julliard (2023) <doi:10.1111/jofi.13197>. In this
package, we provide a novel Bayesian framework for analyzing linear asset
pricing models: simple, robust, and applicable to high-dimensional
problems. For a stand-alone model, we provide functions including
BayesianFM() and BayesianSDF() to deliver reliable price of risk estimates
for both tradable and nontradable factors. For competing factors and
possibly nonnested models, we provide functions including
continuous_ss_sdf(), continuous_ss_sdf_v2(), and dirac_ss_sdf_pvalue() to
analyze high-dimensional models. If you use this package, please cite the
paper. We are thankful to Yunan Ding and Jingtong Zhang for their research
assistance. Any errors or omissions are the responsibility of the authors.

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
