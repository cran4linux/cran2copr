%global __brp_check_rpaths %{nil}
%global packname  fy
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Utilities for Financial Years

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fastmatch 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-hutils 
BuildRequires:    R-utils 
Requires:         R-CRAN-fastmatch 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-hutils 
Requires:         R-utils 

%description
In Australia, a financial year (or fiscal year) is the period from 1 July
to 30 June of the following calendar year. As such, many databases need to
represent and validate financial years efficiently. While the use of
integer years with a convention that they represent the year ending is
common, it may lead to ambiguity with calendar years. On the other hand,
string representations may be too inefficient and do not easily admit
arithmetic operations. This package tries to make validation of financial
years quicker while retaining clarity.

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
