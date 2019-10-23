%global packname  vegtable
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          Handling Vegetation Data Sets

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-taxlist 
BuildRequires:    R-foreign 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plotKML 
BuildRequires:    R-CRAN-qdapRegex 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-vegdata 
Requires:         R-CRAN-taxlist 
Requires:         R-foreign 
Requires:         R-methods 
Requires:         R-CRAN-plotKML 
Requires:         R-CRAN-qdapRegex 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-vegdata 

%description
Import and handling data from vegetation-plot databases, especially data
stored in 'Turboveg' (<https://www.synbiosys.alterra.nl/turboveg>). Also
import/export routines for exchange of data with 'Juice'
(<http://www.sci.muni.cz/botany/juice>) are implemented.

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
%doc %{rlibdir}/%{packname}/Fujiwara_2014
%doc %{rlibdir}/%{packname}/juice
%{rlibdir}/%{packname}/tv_data
%{rlibdir}/%{packname}/INDEX
