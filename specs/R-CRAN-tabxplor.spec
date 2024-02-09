%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tabxplor
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          User-Friendly Tables with Color Helpers for Data Exploration

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats >= 4.0.0
BuildRequires:    R-CRAN-tibble >= 3.1.0
BuildRequires:    R-CRAN-cli >= 2.0.0
BuildRequires:    R-CRAN-pillar >= 1.6.0
BuildRequires:    R-CRAN-magrittr >= 1.5.0
BuildRequires:    R-CRAN-stringi >= 1.4.6
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-crayon >= 1.3.0
BuildRequires:    R-CRAN-kableExtra >= 1.3.0
BuildRequires:    R-CRAN-tidyr >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.3
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-DescTools >= 0.99.0
BuildRequires:    R-CRAN-forcats >= 0.5.0
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-purrr >= 0.3.0
BuildRequires:    R-CRAN-vctrs >= 0.3.0
BuildRequires:    R-CRAN-data.table 
Requires:         R-stats >= 4.0.0
Requires:         R-CRAN-tibble >= 3.1.0
Requires:         R-CRAN-cli >= 2.0.0
Requires:         R-CRAN-pillar >= 1.6.0
Requires:         R-CRAN-magrittr >= 1.5.0
Requires:         R-CRAN-stringi >= 1.4.6
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-crayon >= 1.3.0
Requires:         R-CRAN-kableExtra >= 1.3.0
Requires:         R-CRAN-tidyr >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.0.3
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-DescTools >= 0.99.0
Requires:         R-CRAN-forcats >= 0.5.0
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-purrr >= 0.3.0
Requires:         R-CRAN-vctrs >= 0.3.0
Requires:         R-CRAN-data.table 

%description
Make it easy to deal with multiple cross-tables in data exploration, by
creating them, manipulating them, and adding color helpers to highlight
important informations (differences from totals, comparisons between lines
or columns, contributions to variance, margins of error, etc.). All
functions are pipe-friendly and render data frames which can be easily
manipulated. In the same time, time-taking operations are done with
'data.table' to go faster with big dataframes. Tables can be exported to
'Excel' and in html with formats and colors.

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
