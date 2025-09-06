%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  connector.databricks
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Expand 'connector' Package for 'Databricks' Tables and Volumes

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.4.0
BuildRequires:    R-CRAN-odbc >= 1.4.0
BuildRequires:    R-CRAN-connector >= 1.0.0
BuildRequires:    R-CRAN-brickster >= 0.2.7
BuildRequires:    R-CRAN-arrow 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-dbplyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-hms 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-zephyr 
Requires:         R-CRAN-R6 >= 2.4.0
Requires:         R-CRAN-odbc >= 1.4.0
Requires:         R-CRAN-connector >= 1.0.0
Requires:         R-CRAN-brickster >= 0.2.7
Requires:         R-CRAN-arrow 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-dbplyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-hms 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-zephyr 

%description
Expands the 'connector'
<https://github.com/NovoNordisk-OpenSource/connector> package and provides
a convenient interface for accessing and interacting with 'Databricks'
<https://www.databricks.com> volumes and tables directly from R.

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
