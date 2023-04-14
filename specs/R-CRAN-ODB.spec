%global __brp_check_rpaths %{nil}
%global packname  ODB
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Open Document Databases (.odb) Management

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         zip
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-RJDBC 
BuildRequires:    R-utils 
Requires:         R-methods 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-RJDBC 
Requires:         R-utils 

%description
Functions to create, connect, update and query 'HSQL' databases embedded
in Open Document Databases files, as 'OpenOffice' and 'LibreOffice' do.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
