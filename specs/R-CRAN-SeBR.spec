%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SeBR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Semiparametric Bayesian Regression Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-GpGp 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-spikeSlabGAM 
BuildRequires:    R-CRAN-statmod 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-GpGp 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-spikeSlabGAM 
Requires:         R-CRAN-statmod 

%description
Monte Carlo and MCMC sampling algorithms for semiparametric Bayesian
regression analysis. These models feature a nonparametric (unknown)
transformation of the data paired with widely-used regression models
including linear regression, spline regression, quantile regression, and
Gaussian processes. The transformation enables broader applicability of
these key models, including for real-valued, positive, and
compactly-supported data with challenging distributional features. The
samplers prioritize computational scalability and, for most cases, Monte
Carlo (not MCMC) sampling for greater efficiency. Details of the methods
and algorithms are provided in Kowal and Wu (2023) <arXiv:2306.05498>.

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
