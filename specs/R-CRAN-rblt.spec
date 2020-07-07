%global packname  rblt
%global packver   0.2.4.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4.5
Release:          3%{?dist}
Summary:          Bio-Logging Toolbox

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    hdf5-devel >= 1.8.12
Requires:         hdf5
BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-hdf5r >= 1.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-dygraphs 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-methods 
BuildRequires:    R-tools 
Requires:         R-CRAN-hdf5r >= 1.0
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-dygraphs 
Requires:         R-CRAN-shiny 
Requires:         R-methods 
Requires:         R-tools 

%description
An R-shiny application to plot datalogger time series at a microsecond
precision as Acceleration, Temperature, Pressure, Light intensity from
CATS, AXY-TREK LUL and WACU bio-loggers. It is possible to link behavioral
labels extracted from 'BORIS' software <http://www.boris.unito.it> or
manually written in a csv file. CATS bio-logger are manufactured by
<http://www.cats.is>, AXY-TREK are manufactured by
<http://www.technosmart.eu> and LUL and WACU are manufactured by
<http://www.iphc.cnrs.fr/-MIBE-.html>.

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
%{rlibdir}/%{packname}/INDEX
