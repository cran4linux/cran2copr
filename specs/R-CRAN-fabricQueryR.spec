%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fabricQueryR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Access and Manage 'Microsoft Fabric'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.4.0
BuildRequires:    R-CRAN-reticulate >= 1.41
BuildRequires:    R-CRAN-httr2 >= 1.2.0
BuildRequires:    R-CRAN-nanoarrow >= 0.8.0
BuildRequires:    R-CRAN-rlang >= 0.4.10
BuildRequires:    R-CRAN-AzureAuth 
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.4.0
Requires:         R-CRAN-reticulate >= 1.41
Requires:         R-CRAN-httr2 >= 1.2.0
Requires:         R-CRAN-nanoarrow >= 0.8.0
Requires:         R-CRAN-rlang >= 0.4.10
Requires:         R-CRAN-AzureAuth 
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-jsonlite 
Requires:         R-methods 
Requires:         R-utils 

%description
Access 'Microsoft Fabric' workspaces, items, and workload endpoints
through its web application programming interfaces (APIs). Connect to data
in 'OneLake', 'Lakehouse', 'Warehouse', semantic model, and 'Eventhouse'
items, with support for 'DBI', 'Arrow', 'GraphQL', and 'Spark'. Manage
files, tables, refreshes, jobs, schedules, ingestion, and long-running
operations.

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
