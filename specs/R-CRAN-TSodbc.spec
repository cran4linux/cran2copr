%global packname  TSodbc
%global packver   2015.4-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2015.4.1
Release:          1%{?dist}
Summary:          'TSdbi' Extensions for ODBC

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.8.0
Requires:         R-core >= 2.8.0
BuildArch:        noarch
BuildRequires:    R-CRAN-TSdbi >= 2015.1.1
BuildRequires:    R-CRAN-TSsql >= 2015.1.1
BuildRequires:    R-CRAN-RODBC >= 0.6.0
BuildRequires:    R-CRAN-DBI >= 0.3.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tframe 
BuildRequires:    R-CRAN-tframePlus 
Requires:         R-CRAN-TSdbi >= 2015.1.1
Requires:         R-CRAN-TSsql >= 2015.1.1
Requires:         R-CRAN-RODBC >= 0.6.0
Requires:         R-CRAN-DBI >= 0.3.1
Requires:         R-methods 
Requires:         R-CRAN-tframe 
Requires:         R-CRAN-tframePlus 

%description
An ODBC interface for 'TSdbi'. Comprehensive examples of all the 'TS*'
packages is provided in the vignette Guide.pdf with the 'TSdata' package.

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

%files
%{rlibdir}/%{packname}
