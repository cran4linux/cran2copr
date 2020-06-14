%global packname  electionsBR
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          2%{?dist}
Summary:          R Functions to Download and Clean Brazilian Electoral Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.9.8
BuildRequires:    R-CRAN-haven >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-stats 
Requires:         R-CRAN-data.table >= 1.9.8
Requires:         R-CRAN-haven >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-readr 
Requires:         R-stats 

%description
Offers a set of functions to easily download and clean Brazilian electoral
data from the Superior Electoral Court website. Among others, the package
retrieves data on local and federal elections for all positions (city
councilor, mayor, state deputy, federal deputy, governor, and president)
aggregated by state, city, and electoral zones.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
