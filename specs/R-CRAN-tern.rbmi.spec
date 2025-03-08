%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tern.rbmi
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Create Interface for 'RBMI' and 'tern'

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 2.1.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-rbmi >= 1.2.5
BuildRequires:    R-CRAN-tern >= 0.9.7
BuildRequires:    R-CRAN-rtables >= 0.6.11
BuildRequires:    R-CRAN-broom >= 0.5.4
BuildRequires:    R-CRAN-formatters >= 0.5.10
BuildRequires:    R-CRAN-lifecycle >= 0.2.0
Requires:         R-CRAN-checkmate >= 2.1.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-rbmi >= 1.2.5
Requires:         R-CRAN-tern >= 0.9.7
Requires:         R-CRAN-rtables >= 0.6.11
Requires:         R-CRAN-broom >= 0.5.4
Requires:         R-CRAN-formatters >= 0.5.10
Requires:         R-CRAN-lifecycle >= 0.2.0

%description
'RBMI' implements standard and reference based multiple imputation methods
for continuous longitudinal endpoints (Gower-Page et al. (2022)
<doi:10.21105/joss.04251>). This package provides an interface for 'RBMI'
uses the 'tern' <https://cran.r-project.org/package=tern> framework by Zhu
et al. (2023) and tabulate results easily using 'rtables'
<https://cran.r-project.org/package=rtables> by Becker et al. (2023).

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
