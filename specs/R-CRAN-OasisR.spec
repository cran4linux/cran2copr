%global packname  OasisR
%global packver   3.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.2
Release:          1%{?dist}
Summary:          Outright Tool for the Analysis of Spatial Inequalities andSegregation

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-methods >= 4.0.0
BuildRequires:    R-CRAN-rgdal >= 1.4.8
BuildRequires:    R-CRAN-measurements >= 1.4.0
BuildRequires:    R-CRAN-spdep >= 1.1.3
BuildRequires:    R-CRAN-seg >= 0.5.7
BuildRequires:    R-CRAN-rgeos >= 0.5.3
BuildRequires:    R-CRAN-outliers >= 0.14
Requires:         R-methods >= 4.0.0
Requires:         R-CRAN-rgdal >= 1.4.8
Requires:         R-CRAN-measurements >= 1.4.0
Requires:         R-CRAN-spdep >= 1.1.3
Requires:         R-CRAN-seg >= 0.5.7
Requires:         R-CRAN-rgeos >= 0.5.3
Requires:         R-CRAN-outliers >= 0.14

%description
A set of indexes and tests for the analysis of social segregation.

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

%files
%{rlibdir}/%{packname}
