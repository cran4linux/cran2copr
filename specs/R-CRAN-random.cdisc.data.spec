%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  random.cdisc.data
%global packver   0.3.16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.16
Release:          1%{?dist}%{?buildtag}
Summary:          Create Random ADaM Datasets

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-yaml >= 2.1.19
BuildRequires:    R-CRAN-checkmate >= 2.1.0
BuildRequires:    R-CRAN-lubridate >= 1.7.10
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.4.1
BuildRequires:    R-CRAN-tidyr >= 1.1.4
BuildRequires:    R-CRAN-dplyr >= 1.1.2
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-lifecycle >= 1.0.3
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-yaml >= 2.1.19
Requires:         R-CRAN-checkmate >= 2.1.0
Requires:         R-CRAN-lubridate >= 1.7.10
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.4.1
Requires:         R-CRAN-tidyr >= 1.1.4
Requires:         R-CRAN-dplyr >= 1.1.2
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-lifecycle >= 1.0.3

%description
A set of functions to create random Analysis Data Model (ADaM) datasets
and cached dataset.  ADaM dataset specifications are described by the
Clinical Data Interchange Standards Consortium (CDISC) Analysis Data Model
Team.

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
