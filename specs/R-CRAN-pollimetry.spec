%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pollimetry
%global packver   1.1.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate Pollinator Body Size and Co-Varying Ecological Traits

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-brms >= 2.16.1
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-brms >= 2.16.1
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-lifecycle 

%description
Tools to estimate pollinator body size and co-varying traits. This package
contains Bayesian predictive models of pollinator body size (for bees and
hoverflies) and bee foraging range, as well as preexisting predictive
models for pollinator body size (currently implemented for ants, bees,
butterflies, flies, moths and wasps), bee tongue length, foraging range,
total field nectar loads and wing loading. An additional GitHub repository
<https://github.com/liamkendall/pollimetrydata> provides model objects to
use the bodysize and foraging.range functions internally. The Bayesian
models are described in Kendall et al. (2019) <doi:10.1002/ece3.4835> &
Kendall et al. (2022) <doi:10.1002/ecy.3809>.

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
