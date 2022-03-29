%global __brp_check_rpaths %{nil}
%global packname  broomExtra
%global packver   4.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Enhancements for 'broom' and 'easystats' Package Families

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-performance >= 0.8.0
BuildRequires:    R-CRAN-broom.mixed >= 0.2.9.3
BuildRequires:    R-CRAN-parameters >= 0.17.0
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-performance >= 0.8.0
Requires:         R-CRAN-broom.mixed >= 0.2.9.3
Requires:         R-CRAN-parameters >= 0.17.0
Requires:         R-CRAN-broom 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 

%description
Provides helper functions that assist in data analysis workflows involving
regression analyses. The goal is to combine the functionality offered by
different set of packages ('broom', 'broom.mixed', 'parameters', and
'performance') through a common syntax to return tidy dataframes
containing model parameters and performance measure summaries. The
'grouped_' variants of the generics provides a convenient way to execute
functions across a combination of grouping variable(s) in a dataframe.

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
