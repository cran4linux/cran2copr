%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  duckplyr
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          A 'DuckDB'-Backed Version of 'dplyr'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-dplyr >= 1.1.3
BuildRequires:    R-CRAN-rlang >= 1.0.6
BuildRequires:    R-CRAN-duckdb >= 0.9.1
BuildRequires:    R-CRAN-vctrs >= 0.6.3
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-collections 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr >= 1.1.3
Requires:         R-CRAN-rlang >= 1.0.6
Requires:         R-CRAN-duckdb >= 0.9.1
Requires:         R-CRAN-vctrs >= 0.6.3
Requires:         R-CRAN-cli 
Requires:         R-CRAN-collections 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyselect 
Requires:         R-utils 

%description
A drop-in replacement for 'dplyr', powered by 'DuckDB' for performance.
Also defines a set of generics that provide a low-level implementer's
interface for the high-level user interface of 'dplyr'.

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
