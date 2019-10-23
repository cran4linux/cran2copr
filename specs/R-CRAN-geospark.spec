%global packname  geospark
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          Bring Local Sf to Spark

License:          Apache License (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-dbplyr >= 1.3.0
BuildRequires:    R-CRAN-sparklyr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-dbplyr >= 1.3.0
Requires:         R-CRAN-sparklyr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.3

%description
R binds 'GeoSpark' <http://geospark.datasyslab.org/> extending 'sparklyr'
<https://spark.rstudio.com/> R package to make distributed 'geocomputing'
easier. Sf is a package that provides [simple features]
<https://en.wikipedia.org/wiki/Simple_Features> access for R and which is
a leading 'geospatial' data processing tool. 'Geospark' R package bring
the same simple features access like sf but running on Spark distributed
system.

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
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
