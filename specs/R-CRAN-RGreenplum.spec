%global __brp_check_rpaths %{nil}
%global packname  RGreenplum
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Interface to 'Greenplum' Database

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-RPostgres 
BuildRequires:    R-methods 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-RPostgres 
Requires:         R-methods 

%description
Fully 'DBI'-compliant interface to 'Greenplum' <https://greenplum.org/>,
an open-source parallel database. This is an extension of the 'RPostgres'
package <https://github.com/r-dbi/RPostgres>.

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
