%global __brp_check_rpaths %{nil}
%global packname  ETLUtils
%global packver   1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Utility Functions to Execute Standard Extract/Transform/LoadOperations (using Package 'ff') on Large Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ff >= 4.0.0
BuildRequires:    R-CRAN-bit >= 4.0.0
Requires:         R-CRAN-ff >= 4.0.0
Requires:         R-CRAN-bit >= 4.0.0

%description
Provides functions to facilitate the use of the 'ff' package in
interaction with big data in 'SQL' databases (e.g. in 'Oracle', 'MySQL',
'PostgreSQL', 'Hive') by allowing easy importing directly into 'ffdf'
objects using 'DBI', 'RODBC' and 'RJDBC'. Also contains some basic utility
functions to do fast left outer join merging based on 'match',
factorisation of data and a basic function for re-coding vectors.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
