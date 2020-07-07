%global packname  wql
%global packver   0.4.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.9
Release:          3%{?dist}
Summary:          Exploring Water Quality Monitoring Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 1.0
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-ggplot2 >= 1.0
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-zoo 

%description
Functions to assist in the processing and exploration of data from
environmental monitoring programs. The package name stands for "water
quality" and reflects the original focus on time series data for physical
and chemical properties of water, as well as the biota. Intended for
programs that sample approximately monthly, quarterly or annually at
discrete stations, a feature of many legacy data sets. Most of the
functions should be useful for analysis of similar-frequency time series
regardless of the subject matter.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
