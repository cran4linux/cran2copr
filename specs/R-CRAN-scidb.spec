%global packname  scidb
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          3%{?dist}
Summary:          An R Interface to SciDB

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-openssl 
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-digest 
Requires:         R-methods 
Requires:         R-CRAN-openssl 

%description
An R interface to the 'SciDB' array database <http://scidb.org>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/scidbdoc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
