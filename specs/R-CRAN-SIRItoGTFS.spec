%global packname  SIRItoGTFS
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}
Summary:          Compare SIRI Datasets to GTFS Tables

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-reshape2 >= 1.4.2
BuildRequires:    R-CRAN-sp >= 1.2.5
BuildRequires:    R-CRAN-rgdal >= 1.2
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-CRAN-easycsv >= 1.0.5
BuildRequires:    R-CRAN-dplyr >= 0.7.2
BuildRequires:    R-CRAN-rgeos >= 0.3.23
Requires:         R-CRAN-reshape2 >= 1.4.2
Requires:         R-CRAN-sp >= 1.2.5
Requires:         R-CRAN-rgdal >= 1.2
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-CRAN-easycsv >= 1.0.5
Requires:         R-CRAN-dplyr >= 0.7.2
Requires:         R-CRAN-rgeos >= 0.3.23

%description
Allows the user to compare SIRI (Service Interface for Real Time
Information) data sets to their GTFS (General Transit Feed Specification)
counterparts, a "Request_id" column us needed for the SIRI data frame in
order to subset parts of it for use.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/icon
%{rlibdir}/%{packname}/INDEX
