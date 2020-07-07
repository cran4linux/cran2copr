%global packname  nasapower
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          3%{?dist}
Summary:          NASA POWER API Client

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-APSIM 
BuildRequires:    R-CRAN-crul 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
Requires:         R-CRAN-APSIM 
Requires:         R-CRAN-crul 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-tibble 
Requires:         R-utils 

%description
Client for 'NASA' 'POWER' global meteorology, surface solar energy and
climatology data 'API'.  'POWER' (Prediction Of Worldwide Energy Resource)
data are freely available global meteorology and surface solar energy
climatology data for download with a resolution of 1/2 by 1/2 arc degree
longitude and latitude and are funded through the 'NASA' Earth Science
Directorate Applied Science Program.  For more on the data themselves, a
web-based data viewer and web access, please see
<https://power.larc.nasa.gov/>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/paper
%{rlibdir}/%{packname}/testdata
%doc %{rlibdir}/%{packname}/vector
%{rlibdir}/%{packname}/INDEX
