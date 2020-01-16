%global packname  rdwd
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Select and Download Climate Data from 'DWD' (German WeatherService)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
Requires:         pandoc-citeproc
BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-berryFunctions >= 1.17.0
BuildRequires:    R-CRAN-pbapply 
Requires:         R-CRAN-berryFunctions >= 1.17.0
Requires:         R-CRAN-pbapply 

%description
Handle climate data from the 'DWD' ('Deutscher Wetterdienst', see
<https://www.dwd.de/EN/climate_environment/cdc/cdc.html> for more
information). Choose files with 'selectDWD()', download and process data
sets with 'dataDWD()' and 'readDWD()'.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
