%global packname  rerddap
%global packver   0.6.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.5
Release:          3%{?dist}
Summary:          General Purpose Client for 'ERDDAP' Servers

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-xml2 >= 1.2.0
BuildRequires:    R-CRAN-ncdf4 >= 1.16
BuildRequires:    R-CRAN-data.table >= 1.12.0
BuildRequires:    R-CRAN-crul >= 0.7.4
BuildRequires:    R-CRAN-hoardr >= 0.5.2
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-xml2 >= 1.2.0
Requires:         R-CRAN-ncdf4 >= 1.16
Requires:         R-CRAN-data.table >= 1.12.0
Requires:         R-CRAN-crul >= 0.7.4
Requires:         R-CRAN-hoardr >= 0.5.2
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-utils 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-tibble 

%description
General purpose R client for 'ERDDAP' servers. Includes functions to
search for 'datasets', get summary information on 'datasets', and fetch
'datasets', in either 'csv' or 'netCDF' format. 'ERDDAP' information:
<https://upwell.pfeg.noaa.gov/erddap/information.html>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/vign
%{rlibdir}/%{packname}/INDEX
