%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cdmeta
%global packver   1.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Confidence-Distribution-Based Inference for Random-Effects Meta-Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pimeta >= 1.1.3
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-pimeta >= 1.1.3
Requires:         R-stats 
Requires:         R-graphics 

%description
Computational tools for confidence-distribution-propagation-based
inference in random-effects meta-analysis. Implements
confidence-distribution propagation for frequentist inference in
random-effects meta-analysis. The package samples the between-study
variance from a confidence distribution based on the exact distribution of
Cochran's Q, samples the average effect conditionally on each draw, and
generates the true effect in a future study. It provides prediction
intervals and confidence intervals for the average effect, between-study
variance, between-study standard deviation, and I2. The methods are
described in Noma and Schwarzer (2026) <doi:10.48550/arXiv.2608.26527>.

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
