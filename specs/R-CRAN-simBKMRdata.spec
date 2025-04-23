%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  simBKMRdata
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Helper Functions for Bayesian Kernel Machine Regression

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-stats 

%description
Provides a suite of helper functions to support Bayesian Kernel Machine
Regression (BKMR) analyses in environmental health research. It enables
the simulation of realistic multivariate exposure data using Multivariate
Skewed Gamma distributions, estimation of distributional parameters by
subgroup, and application of adaptive, data-driven thresholds for feature
selection via Posterior Inclusion Probabilities (PIPs). It is especially
suited for handling skewed exposure data and enhancing the
interpretability of BKMR results through principled variable selection.
The methodology is shown in Hasan et. al. (2025)
<doi:10.1101/2025.04.14.25325822>.

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
