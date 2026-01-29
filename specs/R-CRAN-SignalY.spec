%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SignalY
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Signal Extraction from Panel Data via Bayesian Sparse Regression and Spectral Decomposition

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-waveslim >= 1.8.4
BuildRequires:    R-CRAN-EMD >= 1.5.9
BuildRequires:    R-CRAN-urca >= 1.3.3
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
Requires:         R-CRAN-waveslim >= 1.8.4
Requires:         R-CRAN-EMD >= 1.5.9
Requires:         R-CRAN-urca >= 1.3.3
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-parallel 

%description
Provides a comprehensive toolkit for extracting latent signals from panel
data through multivariate time series analysis. Implements spectral
decomposition methods including wavelet multiresolution analysis via
maximal overlap discrete wavelet transform, Percival and Walden (2000)
<doi:10.1017/CBO9780511841040>, empirical mode decomposition for
non-stationary signals, Huang et al. (1998) <doi:10.1098/rspa.1998.0193>,
and Bayesian trend extraction via the Grant-Chan embedded Hodrick-Prescott
filter, Grant and Chan (2017) <doi:10.1016/j.jedc.2016.12.007>. Features
Bayesian variable selection through regularized Horseshoe priors, Piironen
and Vehtari (2017) <doi:10.1214/17-EJS1337SI>, for identifying
structurally relevant predictors from high-dimensional candidate sets.
Includes dynamic factor model estimation, principal component analysis
with bootstrap significance testing, and automated technical
interpretation of signal morphology and variance topology.

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
