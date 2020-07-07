%global packname  epiflows
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}
Summary:          Predicting Disease Spread from Flow Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-epicontacts 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-ggmap 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-visNetwork 
Requires:         R-CRAN-epicontacts 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-ggmap 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-stats 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-visNetwork 

%description
Provides functions and classes designed to handle and visualise
epidemiological flows between locations. Also contains a statistical
method for predicting disease spread from flow data initially described in
Dorigatti et al. (2017) <doi:10.2807/1560-7917.ES.2017.22.28.30572>. This
package is part of the RECON (<http://www.repidemicsconsortium.org/>)
toolkit for outbreak analysis.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
