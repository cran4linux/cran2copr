%global packname  PivotalR
%global packver   0.1.18.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.18.3.1
Release:          1%{?dist}
Summary:          A Fast, Easy-to-Use Tool for Manipulating Tables in Databasesand a Wrapper of MADlib

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-methods 
BuildRequires:    R-Matrix 
Requires:         R-methods 
Requires:         R-Matrix 

%description
Provides an R interface for the Pivotal Data stack running on
'PostgreSQL', 'Greenplum' or 'Apache HAWQ (incubating)' databases with
parallel and distributed computation ability for big data processing.
'PivotalR' provides an R interface to various database operations on
tables or views. These operations are almost the same as the corresponding
native R operations. Thus users of R do not need to learn 'SQL' when they
operate on objects in the database. It also provides a wrapper for 'Apache
MADlib (incubating)', which is an open- source library for parallel and
scalable in-database analytics.

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
%doc %{rlibdir}/%{packname}/dbi
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/gui
%doc %{rlibdir}/%{packname}/sql
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
