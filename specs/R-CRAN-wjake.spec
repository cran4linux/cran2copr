%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wjake
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Personal Themes and Formatting Preferences

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5.0
Requires:         R-core >= 4.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 4.0.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-english 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-CRAN-gh 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-pak 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-showtextdb 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-sysfonts 
BuildRequires:    R-CRAN-systemfonts 
BuildRequires:    R-CRAN-xfun 
Requires:         R-CRAN-ggplot2 >= 4.0.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-english 
Requires:         R-CRAN-ggtext 
Requires:         R-CRAN-gh 
Requires:         R-CRAN-glue 
Requires:         R-grDevices 
Requires:         R-CRAN-gt 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-pak 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-showtextdb 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-sysfonts 
Requires:         R-CRAN-systemfonts 
Requires:         R-CRAN-xfun 

%description
A collection of utility functions, themes, and templates to support
personal data analysis workflows. Includes functions for formatting
numeric values as text, custom themes and color scales for 'ggplot2', and
automatic formatting for tables created with 'gt'.

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
