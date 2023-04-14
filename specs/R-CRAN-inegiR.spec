%global __brp_check_rpaths %{nil}
%global packname  inegiR
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Integrate INEGI’s (Mexican Stats Office) API with R

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-tibbletime 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-tibbletime 

%description
Provides functions to download and parse information from INEGI (Official
Mexican statistics agency). To learn more about the API, see
<https://www.inegi.org.mx/servicios/api_indicadores.html>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
