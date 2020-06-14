%global packname  AeRobiology
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          2%{?dist}
Summary:          A Computational Tool for Aerobiological Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-ggvis 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-ggvis 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-circular 
Requires:         R-CRAN-scales 
Requires:         R-grDevices 
Requires:         R-CRAN-zoo 
Requires:         R-grid 
Requires:         R-CRAN-data.table 

%description
Different tools for managing databases of airborne particles, elaborating
the main calculations and visualization of results. In a first step, data
are checked using tools for quality control and all missing gaps are
completed. Then, the main parameters of the pollen season are calculated
and represented graphically. Multiple graphical tools are available:
pollen calendars, phenological plots, time series, tendencies, interactive
plots, abundance plots...

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
