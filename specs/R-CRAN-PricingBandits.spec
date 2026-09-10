%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PricingBandits
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Armed Bandit Approaches to Pricing Experiments

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-hash 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-TruncatedNormal 
BuildRequires:    R-CRAN-R.utils 
Requires:         R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-hash 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-TruncatedNormal 
Requires:         R-CRAN-R.utils 

%description
Implements multi-armed bandit approaches for pricing experiments with an
unknown demand curve, as developed in Weaver, Kumar, and Jain,
"Nonparametric Pricing Bandits Leveraging Informational Externalities to
Learn the Demand Curve" <doi:10.1287/mksc.2022.0247>. Includes Upper
Confidence Bound (UCB) and Thompson Sampling (TS) baselines, Gaussian
process variants ('GP-UCB', 'GP-TS'), monotonic Gaussian process variants
that constrain demand to be weakly decreasing in price, and
heterogeneous-noise extensions. The willingness-to-pay distribution is
fully user-specified via a vector of consumer valuations, so any demand
environment can be simulated or replayed.

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
