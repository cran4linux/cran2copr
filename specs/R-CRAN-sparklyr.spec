%global packname  sparklyr
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          R Interface to Apache Spark

License:          Apache License 2.0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.4
BuildRequires:    R-CRAN-httr >= 1.2.1
BuildRequires:    R-CRAN-dbplyr >= 1.1.0
BuildRequires:    R-CRAN-openssl >= 0.8
BuildRequires:    R-CRAN-dplyr >= 0.7.2
BuildRequires:    R-CRAN-DBI >= 0.6.1
BuildRequires:    R-CRAN-config >= 0.2
BuildRequires:    R-CRAN-rstudioapi >= 0.10
BuildRequires:    R-CRAN-rlang >= 0.1.4
BuildRequires:    R-CRAN-ellipsis >= 0.1.0
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-forge 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-r2d3 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-rprojroot 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-jsonlite >= 1.4
Requires:         R-CRAN-httr >= 1.2.1
Requires:         R-CRAN-dbplyr >= 1.1.0
Requires:         R-CRAN-openssl >= 0.8
Requires:         R-CRAN-dplyr >= 0.7.2
Requires:         R-CRAN-DBI >= 0.6.1
Requires:         R-CRAN-config >= 0.2
Requires:         R-CRAN-rstudioapi >= 0.10
Requires:         R-CRAN-rlang >= 0.1.4
Requires:         R-CRAN-ellipsis >= 0.1.0
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-forge 
Requires:         R-CRAN-generics 
Requires:         R-methods 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-r2d3 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-rprojroot 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-xml2 

%description
R interface to Apache Spark, a fast and general engine for big data
processing, see <http://spark.apache.org>. This package supports
connecting to local and remote Apache Spark clusters, provides a 'dplyr'
compatible back-end, and provides an interface to Spark's built-in machine
learning algorithms.

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
%doc %{rlibdir}/%{packname}/conf
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/icons
%doc %{rlibdir}/%{packname}/java
%doc %{rlibdir}/%{packname}/livy
%doc %{rlibdir}/%{packname}/rstudio
%doc %{rlibdir}/%{packname}/sparkml
%doc %{rlibdir}/%{packname}/streams
%{rlibdir}/%{packname}/INDEX
