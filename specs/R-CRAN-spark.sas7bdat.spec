%global packname  spark.sas7bdat
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          2%{?dist}
Summary:          Read in 'SAS' Data ('.sas7bdat' Files) into 'Apache Spark'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-sparklyr >= 0.3
Requires:         R-CRAN-sparklyr >= 0.3

%description
Read in 'SAS' Data ('.sas7bdat' Files) into 'Apache Spark' from R. 'Apache
Spark' is an open source cluster computing framework available at
<http://spark.apache.org>. This R package uses the 'spark-sas7bdat'
'Spark' package
(<https://spark-packages.org/package/saurfang/spark-sas7bdat>) to import
and process 'SAS' data in parallel using 'Spark'. Hereby allowing to
execute 'dplyr' statements in parallel on top of 'SAS' data.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
