%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gtreg
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Regulatory Tables for Clinical Research

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.1
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-gtsummary >= 2.0.0
BuildRequires:    R-CRAN-glue >= 1.6.2
BuildRequires:    R-CRAN-stringr >= 1.5.0
BuildRequires:    R-CRAN-tidyr >= 1.2.1
BuildRequires:    R-CRAN-broom.helpers >= 1.13.0
BuildRequires:    R-CRAN-dplyr >= 1.1.1
BuildRequires:    R-CRAN-rlang >= 1.1.1
BuildRequires:    R-CRAN-purrr >= 1.0.1
BuildRequires:    R-CRAN-forcats >= 1.0.0
Requires:         R-CRAN-cli >= 3.6.1
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-gtsummary >= 2.0.0
Requires:         R-CRAN-glue >= 1.6.2
Requires:         R-CRAN-stringr >= 1.5.0
Requires:         R-CRAN-tidyr >= 1.2.1
Requires:         R-CRAN-broom.helpers >= 1.13.0
Requires:         R-CRAN-dplyr >= 1.1.1
Requires:         R-CRAN-rlang >= 1.1.1
Requires:         R-CRAN-purrr >= 1.0.1
Requires:         R-CRAN-forcats >= 1.0.0

%description
Creates tables suitable for regulatory agency submission by leveraging the
'gtsummary' package as the back end. Tables can be exported to HTML, Word,
PDF and more. Highly customized outputs are available by utilizing
existing styling functions from 'gtsummary' as well as custom options
designed for regulatory tables.

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
