%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  remverse
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Comprehensive Tools for Relational Event History Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-remify >= 4.1.0
BuildRequires:    R-CRAN-remstats >= 4.1.0
BuildRequires:    R-CRAN-remstimate >= 3.1.0
BuildRequires:    R-CRAN-remdata >= 0.2.1
Requires:         R-CRAN-remify >= 4.1.0
Requires:         R-CRAN-remstats >= 4.1.0
Requires:         R-CRAN-remstimate >= 3.1.0
Requires:         R-CRAN-remdata >= 0.2.1

%description
A unified interface for relational event history analysis. The package
re-exports key functions from 'remify', 'remstats', and 'remstimate' to
support a streamlined workflow from data processing to model estimation
and diagnosis.

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
