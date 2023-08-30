%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OasisR
%global packver   3.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Outright Tool for the Analysis of Spatial Inequalities and Segregation

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-methods >= 4.3.1
BuildRequires:    R-CRAN-measurements >= 1.5.1
BuildRequires:    R-CRAN-spdep >= 1.2.8
BuildRequires:    R-CRAN-sf >= 1.0.14
BuildRequires:    R-CRAN-seg >= 0.5.7
BuildRequires:    R-CRAN-lwgeom >= 0.2.13
BuildRequires:    R-CRAN-outliers >= 0.15
Requires:         R-methods >= 4.3.1
Requires:         R-CRAN-measurements >= 1.5.1
Requires:         R-CRAN-spdep >= 1.2.8
Requires:         R-CRAN-sf >= 1.0.14
Requires:         R-CRAN-seg >= 0.5.7
Requires:         R-CRAN-lwgeom >= 0.2.13
Requires:         R-CRAN-outliers >= 0.15

%description
A set of indexes and tests for the analysis of social segregation.

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
