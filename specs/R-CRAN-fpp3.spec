%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fpp3
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Data for "Forecasting: Principles and Practice" (3rd Edition)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.1
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-tibble >= 1.4.2
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-cli >= 1.0.0
BuildRequires:    R-CRAN-tsibble >= 0.9.3
BuildRequires:    R-CRAN-tidyr >= 0.8.3
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-rstudioapi >= 0.7
BuildRequires:    R-CRAN-fable >= 0.3.0
BuildRequires:    R-CRAN-fabletools >= 0.3.0
BuildRequires:    R-CRAN-purrr >= 0.2.4
BuildRequires:    R-CRAN-tsibbledata >= 0.2.0
BuildRequires:    R-CRAN-feasts >= 0.1.7
Requires:         R-CRAN-ggplot2 >= 3.1.1
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-tibble >= 1.4.2
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-cli >= 1.0.0
Requires:         R-CRAN-tsibble >= 0.9.3
Requires:         R-CRAN-tidyr >= 0.8.3
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-rstudioapi >= 0.7
Requires:         R-CRAN-fable >= 0.3.0
Requires:         R-CRAN-fabletools >= 0.3.0
Requires:         R-CRAN-purrr >= 0.2.4
Requires:         R-CRAN-tsibbledata >= 0.2.0
Requires:         R-CRAN-feasts >= 0.1.7

%description
All data sets required for the examples and exercises in the book
"Forecasting: principles and practice" by Rob J Hyndman and George
Athanasopoulos <https://OTexts.com/fpp3/>.  All packages required to run
the examples are also loaded.

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
