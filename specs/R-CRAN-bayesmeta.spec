%global __brp_check_rpaths %{nil}
%global packname  bayesmeta
%global packver   2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.7
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Random-Effects Meta-Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-numDeriv >= 2016.8.1.1
BuildRequires:    R-CRAN-forestplot >= 2.0.0
BuildRequires:    R-CRAN-metafor >= 2.0.0
Requires:         R-CRAN-numDeriv >= 2016.8.1.1
Requires:         R-CRAN-forestplot >= 2.0.0
Requires:         R-CRAN-metafor >= 2.0.0

%description
A collection of functions allowing to derive the posterior distribution of
the two parameters in a random-effects meta-analysis, and providing
functionality to evaluate joint and marginal posterior probability
distributions, predictive distributions, shrinkage effects, posterior
predictive p-values, etc.; For more details, see also Roever C (2020)
<doi:10.18637/jss.v093.i06>.

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
