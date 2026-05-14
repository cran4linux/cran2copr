%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shewhartr
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Process Control with Tidyverse-Native Workflows

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-tibble >= 3.2.0
BuildRequires:    R-CRAN-tidyselect >= 1.2.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-purrr >= 1.0.0
BuildRequires:    R-CRAN-broom >= 1.0.0
BuildRequires:    R-CRAN-slider >= 0.3.0
BuildRequires:    R-grid 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-tibble >= 3.2.0
Requires:         R-CRAN-tidyselect >= 1.2.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-purrr >= 1.0.0
Requires:         R-CRAN-broom >= 1.0.0
Requires:         R-CRAN-slider >= 0.3.0
Requires:         R-grid 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 

%description
A comprehensive toolkit for Statistical Process Control (SPC) that
combines the rigor of classical Shewhart methodology with modern
tidyverse-native interfaces. Provides classical control charts for
variables (I-MR, Xbar-R, Xbar-S) and attributes (p, np, c, u), as well as
regression-based control charts for processes with trend. Includes Nelson
runs tests, Average Run Length (ARL) simulation, process capability
indices with bootstrap confidence intervals, Box-Cox transformation
guidance, and a clean Phase I / Phase II workflow. All chart objects
integrate with broom via 'tidy', 'glance' and 'augment' methods.
References: Shewhart (1931, ISBN:0-87389-076-0); Montgomery (2019,
ISBN:978-1-119-39930-8); Nelson (1984)
<doi:10.1080/00224065.1984.11978921>; Woodall (2000)
<doi:10.1080/00224065.2000.11980013>; Box & Cox (1964)
<doi:10.1111/j.2517-6161.1964.tb00553.x>.

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
