%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lares
%global packver   5.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Lean Analytics and Robust Exploration Sidekick

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rpart >= 4.1.0
BuildRequires:    R-CRAN-openxlsx >= 3.5.10
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-rpart.plot >= 3.1.0
BuildRequires:    R-CRAN-yaml >= 2.2.4
BuildRequires:    R-CRAN-jsonlite >= 1.8.0
BuildRequires:    R-CRAN-lubridate >= 1.7.9
BuildRequires:    R-CRAN-httr >= 1.4.3
BuildRequires:    R-CRAN-stringr >= 1.4.2
BuildRequires:    R-CRAN-patchwork >= 1.3.0
BuildRequires:    R-CRAN-pROC >= 1.18.5
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-rvest >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.6.3
Requires:         R-CRAN-rpart >= 4.1.0
Requires:         R-CRAN-openxlsx >= 3.5.10
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-rpart.plot >= 3.1.0
Requires:         R-CRAN-yaml >= 2.2.4
Requires:         R-CRAN-jsonlite >= 1.8.0
Requires:         R-CRAN-lubridate >= 1.7.9
Requires:         R-CRAN-httr >= 1.4.3
Requires:         R-CRAN-stringr >= 1.4.2
Requires:         R-CRAN-patchwork >= 1.3.0
Requires:         R-CRAN-pROC >= 1.18.5
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-rvest >= 1.0.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-rlang >= 0.6.3

%description
Auxiliary package for better/faster analytics, visualization, data mining,
and machine learning tasks. With a wide variety of family functions, like
Machine Learning, Data Wrangling, Marketing Mix Modeling (Robyn),
Exploratory, API, and Scrapper, it helps the analyst or data scientist to
get quick and robust results, without the need of repetitive coding or
advanced R programming skills.

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
