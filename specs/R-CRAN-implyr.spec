%global packname  implyr
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          R Interface for Apache Impala

License:          Apache License 2.0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-dbplyr >= 1.2.1
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-DBI >= 0.7
BuildRequires:    R-CRAN-tidyselect >= 0.2.3
BuildRequires:    R-CRAN-rlang >= 0.1.6
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-dbplyr >= 1.2.1
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-DBI >= 0.7
Requires:         R-CRAN-tidyselect >= 0.2.3
Requires:         R-CRAN-rlang >= 0.1.6
Requires:         R-CRAN-assertthat 
Requires:         R-methods 
Requires:         R-utils 

%description
'SQL' back-end to 'dplyr' for Apache Impala, the massively parallel
processing query engine for Apache 'Hadoop'. Impala enables low-latency
'SQL' queries on data stored in the 'Hadoop' Distributed File System
'(HDFS)', Apache 'HBase', Apache 'Kudu', Amazon Simple Storage Service
'(S3)', Microsoft Azure Data Lake Store '(ADLS)', and Dell 'EMC' 'Isilon'.
See <https://impala.apache.org> for more information about Impala.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
