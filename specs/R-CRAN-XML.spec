%global packname  XML
%global packver   3.99-0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.99.0.2
Release:          1%{?dist}
Summary:          Tools for Parsing and Generating XML Within R and S-Plus

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    libxml2-devel >= 2.6.3
Requires:         libxml2
BuildRequires:    R-devel >= 2.13.0
Requires:         R-core >= 2.13.0
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-methods 
Requires:         R-utils 

%description
Many approaches for both reading and creating XML (and HTML) documents
(including DTDs), both local and accessible via HTTP or FTP.  Also offers
access to an 'XPath' "interpreter".

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/exampleData
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/FAQ.html
%doc %{rlibdir}/%{packname}/scripts
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
