%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggblanket
%global packver   12.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          12.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simplify 'ggplot2' Visualisation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.1
BuildRequires:    R-CRAN-lubridate >= 1.7.8
BuildRequires:    R-CRAN-scales >= 1.3.0
BuildRequires:    R-CRAN-stringr >= 1.3.0
BuildRequires:    R-CRAN-tidyselect >= 1.2.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.4
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-hms >= 0.5.0
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-farver 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-ggblend 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-labelled 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-snakecase 
BuildRequires:    R-CRAN-viridisLite 
Requires:         R-CRAN-ggplot2 >= 3.5.1
Requires:         R-CRAN-lubridate >= 1.7.8
Requires:         R-CRAN-scales >= 1.3.0
Requires:         R-CRAN-stringr >= 1.3.0
Requires:         R-CRAN-tidyselect >= 1.2.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.0.4
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-hms >= 0.5.0
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-farver 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-ggblend 
Requires:         R-grid 
Requires:         R-CRAN-labelled 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-snakecase 
Requires:         R-CRAN-viridisLite 

%description
Simplify 'ggplot2' visualisation with 'ggblanket' wrapper functions.

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
