%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tuneRanger
%global packver   0.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tune Random Forest of the 'ranger' Package

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-parallel >= 3.3.3
BuildRequires:    R-methods >= 3.3.3
BuildRequires:    R-CRAN-mlr >= 2.11
BuildRequires:    R-CRAN-DiceKriging >= 1.5.5
BuildRequires:    R-CRAN-smoof >= 1.5.1
BuildRequires:    R-CRAN-BBmisc >= 1.11
BuildRequires:    R-CRAN-ParamHelpers >= 1.10
BuildRequires:    R-CRAN-mlrMBO >= 1.1.1
BuildRequires:    R-CRAN-ranger >= 0.8.0
BuildRequires:    R-CRAN-lhs >= 0.14
Requires:         R-parallel >= 3.3.3
Requires:         R-methods >= 3.3.3
Requires:         R-CRAN-mlr >= 2.11
Requires:         R-CRAN-DiceKriging >= 1.5.5
Requires:         R-CRAN-smoof >= 1.5.1
Requires:         R-CRAN-BBmisc >= 1.11
Requires:         R-CRAN-ParamHelpers >= 1.10
Requires:         R-CRAN-mlrMBO >= 1.1.1
Requires:         R-CRAN-ranger >= 0.8.0
Requires:         R-CRAN-lhs >= 0.14

%description
Tuning random forest with one line. The package is mainly based on the
packages 'ranger' and 'mlrMBO'.

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
