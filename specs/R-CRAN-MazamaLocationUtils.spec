%global packname  MazamaLocationUtils
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          2%{?dist}
Summary:          Manage Spatial Metadata for Known Locations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-geodist 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-MazamaCoreUtils 
BuildRequires:    R-CRAN-MazamaSpatialUtils 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-revgeo 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-geodist 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-lubridate 
Requires:         R-methods 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-MazamaCoreUtils 
Requires:         R-CRAN-MazamaSpatialUtils 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-revgeo 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 

%description
A suite of utility functions for discovering and managing metadata
associated with sets of spatially unique "known locations".

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
