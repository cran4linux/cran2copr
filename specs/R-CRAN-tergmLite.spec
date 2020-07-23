%global packname  tergmLite
%global packver   2.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          1%{?dist}
Summary:          Fast Simulation of Simple Temporal Exponential Random GraphModels

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-statnet.common >= 4.3.0
BuildRequires:    R-CRAN-tergm >= 3.6.1
BuildRequires:    R-CRAN-ergm >= 3.10.4
BuildRequires:    R-CRAN-network >= 1.16.0
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-statnet.common >= 4.3.0
Requires:         R-CRAN-tergm >= 3.6.1
Requires:         R-CRAN-ergm >= 3.10.4
Requires:         R-CRAN-network >= 1.16.0
Requires:         R-CRAN-Rcpp 

%description
Provides functions for the computationally efficient simulation of dynamic
networks estimated with the statistical framework of temporal exponential
random graph models, implemented in the 'tergm' package.

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
