%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tdcmStan
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automating the Creation of Stan Code for TDCMs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-parallel >= 4.1.0
BuildRequires:    R-CRAN-tibble >= 3.1.5
BuildRequires:    R-CRAN-magrittr >= 2.0.1
BuildRequires:    R-CRAN-glue >= 1.4.2
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-tidyr >= 1.1.4
BuildRequires:    R-CRAN-tidyselect >= 1.1.2
BuildRequires:    R-CRAN-dplyr >= 1.0.7
BuildRequires:    R-CRAN-rlang >= 0.4.11
Requires:         R-parallel >= 4.1.0
Requires:         R-CRAN-tibble >= 3.1.5
Requires:         R-CRAN-magrittr >= 2.0.1
Requires:         R-CRAN-glue >= 1.4.2
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-tidyr >= 1.1.4
Requires:         R-CRAN-tidyselect >= 1.1.2
Requires:         R-CRAN-dplyr >= 1.0.7
Requires:         R-CRAN-rlang >= 0.4.11

%description
A collection of functions for automatically creating 'Stan' code for
transition diagnostic classification models (TDCMs) as they are defined by
Madison and Bradshaw (2018) <DOI:10.1007/s11336-018-9638-5>. This package
supports automating the creation of 'Stan' code for TDCMs, fungible TDCMs
(i.e., TDCMs with item parameters constrained to be equal across all
items), and multi-threaded TDCMs.

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
