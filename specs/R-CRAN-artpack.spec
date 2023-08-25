%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  artpack
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Creates Generative Art Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.1.6
BuildRequires:    R-CRAN-stringr >= 1.5.0
BuildRequires:    R-CRAN-dplyr >= 1.0.8
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-tibble >= 3.1.6
Requires:         R-CRAN-stringr >= 1.5.0
Requires:         R-CRAN-dplyr >= 1.0.8
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-cli 
Requires:         R-grDevices 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rlang 

%description
Create data that displays generative art when mapped into a 'ggplot2'
plot. Functionality includes specialized data frame creation for geometric
shapes, tools that define artistic color palettes, tools for geometrically
transforming data, and other miscellaneous tools that are helpful when
using 'ggplot2' for generative art.

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
