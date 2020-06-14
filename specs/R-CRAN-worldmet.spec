%global packname  worldmet
%global packver   0.8.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.8
Release:          2%{?dist}
Summary:          Import Surface Meteorological Data from NOAA Integrated SurfaceDatabase (ISD)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-openair 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-openair 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-zoo 

%description
Functions to import data from more than 30,000 surface meteorological
sites around the world managed by the National Oceanic and Atmospheric
Administration (NOAA) Integrated Surface Database (ISD, see
<https://www.ncdc.noaa.gov/isd>).

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/images
%{rlibdir}/%{packname}/INDEX
