%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  growthcleanr
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Data Cleaner for Anthropometric Measurements

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-labelled >= 2.5.0
BuildRequires:    R-CRAN-R.utils >= 2.11.0
BuildRequires:    R-CRAN-plyr >= 1.8.6
BuildRequires:    R-CRAN-foreach >= 1.5.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-data.table >= 1.13.0
BuildRequires:    R-CRAN-tidyr >= 1.1.0
BuildRequires:    R-CRAN-doParallel >= 1.0.15
BuildRequires:    R-CRAN-dplyr >= 1.0.1
Requires:         R-CRAN-labelled >= 2.5.0
Requires:         R-CRAN-R.utils >= 2.11.0
Requires:         R-CRAN-plyr >= 1.8.6
Requires:         R-CRAN-foreach >= 1.5.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-data.table >= 1.13.0
Requires:         R-CRAN-tidyr >= 1.1.0
Requires:         R-CRAN-doParallel >= 1.0.15
Requires:         R-CRAN-dplyr >= 1.0.1

%description
Identifies implausible anthropometric (e.g., height, weight) measurements
in irregularly spaced longitudinal datasets, such as those from electronic
health records.

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
