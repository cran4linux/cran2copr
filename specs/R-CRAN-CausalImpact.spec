%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CausalImpact
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Inferring Causal Effects using Bayesian Structural Time-Series Models

License:          Apache License 2.0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-bsts >= 0.9.0
BuildRequires:    R-CRAN-assertthat >= 0.2.0
BuildRequires:    R-CRAN-Boom 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-bsts >= 0.9.0
Requires:         R-CRAN-assertthat >= 0.2.0
Requires:         R-CRAN-Boom 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-zoo 

%description
Implements a Bayesian approach to causal impact estimation in time series,
as described in Brodersen et al. (2015) <DOI:10.1214/14-AOAS788>. See the
package documentation on GitHub <https://google.github.io/CausalImpact/>
to get started.

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
