%global packname  ergm.ego
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Fit, Simulate and Diagnose Exponential-Family Random Graph Models to Egocentrically Sampled Network Data

License:          GPL-3 + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-statnet.common >= 4.2.0
BuildRequires:    R-CRAN-ergm >= 3.10.1
BuildRequires:    R-CRAN-tibble >= 2.1.1
BuildRequires:    R-CRAN-network >= 1.15
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-rlang >= 0.3.4
BuildRequires:    R-CRAN-purrr >= 0.3.2
BuildRequires:    R-CRAN-coda >= 0.19.2
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-statnet.common >= 4.2.0
Requires:         R-CRAN-ergm >= 3.10.1
Requires:         R-CRAN-tibble >= 2.1.1
Requires:         R-CRAN-network >= 1.15
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-rlang >= 0.3.4
Requires:         R-CRAN-purrr >= 0.3.2
Requires:         R-CRAN-coda >= 0.19.2
Requires:         R-stats 
Requires:         R-methods 

%description
Utilities for managing egocentrically sampled network data and a wrapper
around the 'ergm' package to facilitate ERGM inference and simulation from
such data.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
