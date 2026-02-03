%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fluxfixer
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Advanced Framework for Sap Flow Data Post-Process

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-stats >= 4.0.3
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-zoo >= 1.8.8
BuildRequires:    R-CRAN-lubridate >= 1.7.9
BuildRequires:    R-CRAN-tidyselect >= 1.2.0
BuildRequires:    R-CRAN-tidyr >= 1.1.4
BuildRequires:    R-CRAN-rlang >= 1.1.3
BuildRequires:    R-CRAN-dplyr >= 1.0.7
BuildRequires:    R-CRAN-gsignal >= 0.3.4
BuildRequires:    R-CRAN-ranger >= 0.13.1
BuildRequires:    R-CRAN-xts >= 0.12.1
Requires:         R-stats >= 4.0.3
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-zoo >= 1.8.8
Requires:         R-CRAN-lubridate >= 1.7.9
Requires:         R-CRAN-tidyselect >= 1.2.0
Requires:         R-CRAN-tidyr >= 1.1.4
Requires:         R-CRAN-rlang >= 1.1.3
Requires:         R-CRAN-dplyr >= 1.0.7
Requires:         R-CRAN-gsignal >= 0.3.4
Requires:         R-CRAN-ranger >= 0.13.1
Requires:         R-CRAN-xts >= 0.12.1

%description
Provides a flexible framework for post-processing thermal dissipation sap
flow data using statistical methods and machine learning. This framework
includes anomaly correction, outlier removal, gap-filling, trend removal,
signal damping correction, and sap flux density calculation. The functions
in this package can also apply to other time series with various
artifacts.

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
