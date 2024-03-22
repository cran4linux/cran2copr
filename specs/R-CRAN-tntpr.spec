%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tntpr
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Data Analysis Tools Customized for TNTP

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.2.1
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-purrr >= 0.3.3
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-extrafont 
BuildRequires:    R-CRAN-formattable 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-keyring 
BuildRequires:    R-CRAN-labelled 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-ggplot2 >= 3.2.1
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-purrr >= 0.3.3
Requires:         R-CRAN-cli 
Requires:         R-CRAN-extrafont 
Requires:         R-CRAN-formattable 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-keyring 
Requires:         R-CRAN-labelled 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tidyselect 

%description
An assortment of functions and templates customized to meet the needs of
data analysts at the non-profit organization TNTP. Includes functions for
branded colors and plots, credentials management, repository set-up, and
other common analytic tasks.

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
