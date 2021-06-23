%global __brp_check_rpaths %{nil}
%global packname  AWR.Kinesis
%global packver   1.7.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.3
Release:          3%{?dist}%{?buildtag}
Summary:          Amazon 'Kinesis' Consumer Application for Stream Processing

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-AWR 
BuildRequires:    R-CRAN-futile.logger 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rJava 
Requires:         R-CRAN-AWR 
Requires:         R-CRAN-futile.logger 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rJava 

%description
Fetching data from Amazon 'Kinesis' Streams using the Java-based
'MultiLangDaemon' interacting with Amazon Web Services ('AWS') for easy
stream processing from R. For more information on 'Kinesis', see
<https://aws.amazon.com/kinesis>.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/java
%{rlibdir}/%{packname}/INDEX
