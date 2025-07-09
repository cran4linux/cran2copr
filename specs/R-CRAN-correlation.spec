%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  correlation
%global packver   0.8.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.8
Release:          1%{?dist}%{?buildtag}
Summary:          Methods for Correlation Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-insight >= 1.3.1
BuildRequires:    R-CRAN-datawizard >= 1.1.0
BuildRequires:    R-CRAN-parameters >= 0.26.0
BuildRequires:    R-CRAN-bayestestR >= 0.16.0
BuildRequires:    R-datasets 
BuildRequires:    R-stats 
Requires:         R-CRAN-insight >= 1.3.1
Requires:         R-CRAN-datawizard >= 1.1.0
Requires:         R-CRAN-parameters >= 0.26.0
Requires:         R-CRAN-bayestestR >= 0.16.0
Requires:         R-datasets 
Requires:         R-stats 

%description
Lightweight package for computing different kinds of correlations, such as
partial correlations, Bayesian correlations, multilevel correlations,
polychoric correlations, biweight correlations, distance correlations and
more. Part of the 'easystats' ecosystem. References: Makowski et al.
(2020) <doi:10.21105/joss.02306>.

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
