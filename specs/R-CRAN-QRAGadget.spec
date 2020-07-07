%global packname  QRAGadget
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          A 'Shiny' Gadget for Interactive 'QRA' Visualizations

License:          Apache License | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-miniUI 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-sp 

%description
Upload raster data and easily create interactive quantitative risk
analysis 'QRA' visualizations. Select from numerous color palettes,
base-maps, and different configurations.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/images
%doc %{rlibdir}/%{packname}/rstudio
%doc %{rlibdir}/%{packname}/tableinput
%{rlibdir}/%{packname}/INDEX
