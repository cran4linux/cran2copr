%global packname  vetools
%global packver   1.3-28
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.28
Release:          2%{?dist}
Summary:          Tools for Venezuelan Environmental Data

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tis 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tis 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-scales 

%description
Integrated data management library that offers a variety of tools
concerning the loading and manipulation of environmental data available
from different Venezuelan governmental sources. Facilities are provided to
plot temporal and spatial data as well as understand the health of a
collection of meteorological data.

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
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/shape
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
