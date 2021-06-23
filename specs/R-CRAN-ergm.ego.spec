%global __brp_check_rpaths %{nil}
%global packname  ergm.ego
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fit, Simulate and Diagnose Exponential-Family Random Graph Models to Egocentrically Sampled Network Data

License:          GPL-3 + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-statnet.common >= 4.5.0
BuildRequires:    R-CRAN-ergm >= 4.0.0
BuildRequires:    R-CRAN-tibble >= 2.1.1
BuildRequires:    R-CRAN-network >= 1.17.1
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-purrr >= 0.3.2
BuildRequires:    R-CRAN-coda >= 0.19.2
BuildRequires:    R-CRAN-egor 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-statnet.common >= 4.5.0
Requires:         R-CRAN-ergm >= 4.0.0
Requires:         R-CRAN-tibble >= 2.1.1
Requires:         R-CRAN-network >= 1.17.1
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-purrr >= 0.3.2
Requires:         R-CRAN-coda >= 0.19.2
Requires:         R-CRAN-egor 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-survey 
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
