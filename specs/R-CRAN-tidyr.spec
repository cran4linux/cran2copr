%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tidyr
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tidy Messy Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildRequires:    R-CRAN-cli >= 3.4.1
BuildRequires:    R-CRAN-tibble >= 2.1.1
BuildRequires:    R-CRAN-stringr >= 1.5.0
BuildRequires:    R-CRAN-tidyselect >= 1.2.0
BuildRequires:    R-CRAN-rlang >= 1.1.1
BuildRequires:    R-CRAN-lifecycle >= 1.0.3
BuildRequires:    R-CRAN-dplyr >= 1.0.10
BuildRequires:    R-CRAN-purrr >= 1.0.1
BuildRequires:    R-CRAN-vctrs >= 0.5.2
BuildRequires:    R-CRAN-cpp11 >= 0.4.0
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.4.1
Requires:         R-CRAN-tibble >= 2.1.1
Requires:         R-CRAN-stringr >= 1.5.0
Requires:         R-CRAN-tidyselect >= 1.2.0
Requires:         R-CRAN-rlang >= 1.1.1
Requires:         R-CRAN-lifecycle >= 1.0.3
Requires:         R-CRAN-dplyr >= 1.0.10
Requires:         R-CRAN-purrr >= 1.0.1
Requires:         R-CRAN-vctrs >= 0.5.2
Requires:         R-CRAN-glue 
Requires:         R-CRAN-magrittr 
Requires:         R-utils 

%description
Tools to help to create tidy data, where each column is a variable, each
row is an observation, and each cell contains a single value.  'tidyr'
contains tools for changing the shape (pivoting) and hierarchy (nesting
and 'unnesting') of a dataset, turning deeply nested lists into
rectangular data frames ('rectangling'), and extracting values out of
string columns. It also includes tools for working with missing values
(both implicit and explicit).

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
