%global __brp_check_rpaths %{nil}
%global packname  sparkavro
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Load Avro file into 'Apache Spark'

License:          Apache License 2.0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-sparklyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DBI 
Requires:         R-CRAN-sparklyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DBI 

%description
Load Avro Files into 'Apache Spark' using 'sparklyr'. This allows to read
files from 'Apache Avro' <https://avro.apache.org/>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
