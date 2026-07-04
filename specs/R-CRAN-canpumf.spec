%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  canpumf
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          Parse StatCan PUMF Files

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-haven >= 2.5.0
BuildRequires:    R-CRAN-duckdb >= 1.5.2
BuildRequires:    R-CRAN-duckplyr >= 1.2.1
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-dbplyr 
BuildRequires:    R-CRAN-zip 
Requires:         R-CRAN-haven >= 2.5.0
Requires:         R-CRAN-duckdb >= 1.5.2
Requires:         R-CRAN-duckplyr >= 1.2.1
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-readr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rlang 
Requires:         R-utils 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-dbplyr 
Requires:         R-CRAN-zip 

%description
Facilitate working with Statistics Canada (StatCan) Public Use Microdata
Files (PUMF). Enables downloading of available PUMF data, parsing of
metadata from command files or other sources to infer the layout
structure, variable labels and value labels as well as missing data
values, and returns a connection to a 'DuckDB' database with the labelled
data. Data and documentation come from Statistics Canada's Public Use
Microdata Files <https://www.statcan.gc.ca/en/microdata/pumf>, distributed
under the Statistics Canada Open Licence
<https://www.statcan.gc.ca/en/terms-conditions/open-licence>.

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
