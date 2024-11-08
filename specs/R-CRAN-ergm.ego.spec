%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ergm.ego
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fit, Simulate and Diagnose Exponential-Family Random Graph Models to Egocentrically Sampled Network Data

License:          GPL-3 + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-ergm >= 4.7.1
BuildRequires:    R-CRAN-survey >= 4.4.2
BuildRequires:    R-CRAN-statnet.common >= 4.10.0
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-egor >= 1.24.2
BuildRequires:    R-CRAN-network >= 1.18.2
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.3
BuildRequires:    R-CRAN-purrr >= 1.0.2
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-ergm >= 4.7.1
Requires:         R-CRAN-survey >= 4.4.2
Requires:         R-CRAN-statnet.common >= 4.10.0
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-egor >= 1.24.2
Requires:         R-CRAN-network >= 1.18.2
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-RColorBrewer >= 1.1.3
Requires:         R-CRAN-purrr >= 1.0.2
Requires:         R-stats 
Requires:         R-methods 

%description
Utilities for managing egocentrically sampled network data and a wrapper
around the 'ergm' package to facilitate ERGM inference and simulation from
such data. See Krivitsky and Morris (2017) <doi:10.1214/16-AOAS1010>.

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
