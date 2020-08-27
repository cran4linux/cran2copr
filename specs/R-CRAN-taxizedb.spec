%global packname  taxizedb
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Working with 'Taxonomic' Databases

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 2.4
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-RSQLite >= 1.1.2
BuildRequires:    R-CRAN-readr >= 1.1.1
BuildRequires:    R-CRAN-dbplyr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-DBI >= 0.6.1
BuildRequires:    R-CRAN-hoardr >= 0.1.0
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-curl >= 2.4
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-RSQLite >= 1.1.2
Requires:         R-CRAN-readr >= 1.1.1
Requires:         R-CRAN-dbplyr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-DBI >= 0.6.1
Requires:         R-CRAN-hoardr >= 0.1.0
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rlang 

%description
Tools for working with 'taxonomic' databases, including utilities for
downloading databases, loading them into various 'SQL' databases, cleaning
up files, and providing a 'SQL' connection that can be used to do 'SQL'
queries directly or used in 'dplyr'.

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
