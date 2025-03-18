%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pacta.loanbook
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Easily Install and Load PACTA for Banks Packages

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-r2dii.data >= 0.6.0
BuildRequires:    R-CRAN-r2dii.analysis >= 0.5.1
BuildRequires:    R-CRAN-r2dii.plot >= 0.5.1
BuildRequires:    R-CRAN-r2dii.match >= 0.4.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-r2dii.data >= 0.6.0
Requires:         R-CRAN-r2dii.analysis >= 0.5.1
Requires:         R-CRAN-r2dii.plot >= 0.5.1
Requires:         R-CRAN-r2dii.match >= 0.4.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyselect 

%description
PACTA (Paris Agreement Capital Transition Assessment) for Banks is a tool
that allows banks to calculate the climate alignment of their corporate
lending portfolios. This package is designed to make it easy to install
and load multiple PACTA for Banks packages in a single step. It also
provides thorough documentation - the PACTA for Banks cookbook at
<https://rmi-pacta.github.io/pacta.loanbook/articles/cookbook_overview.html>
- on how to run a PACTA for Banks analysis. This covers prerequisites for
the analysis, the separate steps of running the analysis, the
interpretation of PACTA for Banks results, and advanced use cases.

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
