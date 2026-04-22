%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spada
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          A 'shiny' Package for Data Analysis

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 4.0.1
BuildRequires:    R-CRAN-haven >= 2.5.5
BuildRequires:    R-CRAN-mirai >= 2.5.3
BuildRequires:    R-CRAN-collapse >= 2.1.6
BuildRequires:    R-CRAN-gt >= 1.3.0
BuildRequires:    R-CRAN-data.table >= 1.18.2.1
BuildRequires:    R-CRAN-shiny >= 1.12.1
BuildRequires:    R-CRAN-rlang >= 1.1.7
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-DescTools >= 0.99.60
BuildRequires:    R-CRAN-shinyWidgets >= 0.9.0
BuildRequires:    R-CRAN-htmltools >= 0.5.9
BuildRequires:    R-CRAN-sass >= 0.4.10
BuildRequires:    R-CRAN-waiter >= 0.2.5.1
BuildRequires:    R-CRAN-bslib >= 0.10.0
BuildRequires:    R-CRAN-qs2 >= 0.1.7
BuildRequires:    R-CRAN-bsicons >= 0.1.2
Requires:         R-CRAN-ggplot2 >= 4.0.1
Requires:         R-CRAN-haven >= 2.5.5
Requires:         R-CRAN-mirai >= 2.5.3
Requires:         R-CRAN-collapse >= 2.1.6
Requires:         R-CRAN-gt >= 1.3.0
Requires:         R-CRAN-data.table >= 1.18.2.1
Requires:         R-CRAN-shiny >= 1.12.1
Requires:         R-CRAN-rlang >= 1.1.7
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-DescTools >= 0.99.60
Requires:         R-CRAN-shinyWidgets >= 0.9.0
Requires:         R-CRAN-htmltools >= 0.5.9
Requires:         R-CRAN-sass >= 0.4.10
Requires:         R-CRAN-waiter >= 0.2.5.1
Requires:         R-CRAN-bslib >= 0.10.0
Requires:         R-CRAN-qs2 >= 0.1.7
Requires:         R-CRAN-bsicons >= 0.1.2

%description
Provides a 'shiny' application with a user-friendly interface for
interactive data analysis. It supports exploratory data analysis through
descriptive statistics, data visualization, statistical tests (e.g.,
normality assessment), linear modeling, data import, transformation and
reporting. For more details see Shapiro and Wilk (1965)
<doi:10.2307/2333709>.

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
