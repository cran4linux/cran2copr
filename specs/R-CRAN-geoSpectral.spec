%global packname  geoSpectral
%global packver   0.17.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.17.5
Release:          1%{?dist}
Summary:          Classes and Methods for Working with Spectral Data withSpace-Time Attributes

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-spacetime 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-rbokeh 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
Requires:         R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-spacetime 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-rbokeh 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-sp 
Requires:         R-stats 

%description
Provides S4 classes and data import, preprocessing, graphing, manipulation
and export methods for geo-Spectral datasets (datasets with
space/time/spectral dimensions). These type of data are frequently
collected within earth observation projects (remote sensing, spectroscopy,
bio-optical oceanography, mining, agricultural, atmospheric, environmental
or similar branch of science).

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/anap.txt
%{rlibdir}/%{packname}/test_data
%{rlibdir}/%{packname}/INDEX
