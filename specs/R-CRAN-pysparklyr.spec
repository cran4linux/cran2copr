%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pysparklyr
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Provides a 'PySpark' Back-End for the 'sparklyr' Package

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-sparklyr >= 1.8.5
BuildRequires:    R-CRAN-reticulate >= 1.33
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-dbplyr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-rsconnect 
Requires:         R-CRAN-sparklyr >= 1.8.5
Requires:         R-CRAN-reticulate >= 1.33
Requires:         R-CRAN-cli 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-dbplyr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-purrr 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-processx 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-rsconnect 

%description
It enables 'sparklyr' to integrate with 'Spark Connect', and 'Databricks
Connect' by providing a wrapper over the 'PySpark' 'python' library.

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
