%global packname  IRISMustangMetrics
%global packver   2.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.0
Release:          3%{?dist}
Summary:          Statistics and Metrics for Seismic Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-IRISSeismic >= 1.3.0
BuildRequires:    R-CRAN-seismicRoll >= 1.1.2
BuildRequires:    R-CRAN-dplyr >= 0.4.3
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-IRISSeismic >= 1.3.0
Requires:         R-CRAN-seismicRoll >= 1.1.2
Requires:         R-CRAN-dplyr >= 0.4.3
Requires:         R-methods 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-XML 
Requires:         R-stats 
Requires:         R-CRAN-pracma 

%description
Classes and functions for metrics calculation as part of the 'IRIS DMC
MUSTANG' project. The functionality in this package builds upon the base
classes of the 'IRISSeismic' package. Metrics include basic statistics as
well as higher level 'health' metrics that can help identify problematic
seismometers.

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
%{rlibdir}/%{packname}/INDEX
