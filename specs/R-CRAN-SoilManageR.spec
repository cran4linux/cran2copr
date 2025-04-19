%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SoilManageR
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate Soil Management Indicators for Agricultural Practice Assessment

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggthemes >= 5.0.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.4
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-Rdpack >= 2.6
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-lubridate >= 1.9.2
BuildRequires:    R-CRAN-readxl >= 1.4.3
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-ggthemes >= 5.0.0
Requires:         R-CRAN-ggplot2 >= 3.4.4
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-Rdpack >= 2.6
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-lubridate >= 1.9.2
Requires:         R-CRAN-readxl >= 1.4.3
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-dplyr >= 1.1.4

%description
Calculate numerical agricultural soil management indicators from on a
management timeline of an arable field. Currently, indicators for carbon
(C) input into the soil system, soil tillage intensity rating (STIR),
number of soil cover and living plant cover days, N fertilization and
livestock intensity, and plant diversity are implemented. The functions
can also be used independently of the management timeline to calculate
some indicators. The package contains tables with reference information
for the functions, as well as a '*.xlsx' template to collect the
management data.

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
