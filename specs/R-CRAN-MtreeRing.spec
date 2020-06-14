%global packname  MtreeRing
%global packver   1.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.2
Release:          2%{?dist}
Summary:          A Shiny Application for Automatic Measurements of Tree-RingWidths on Digital Images

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-tiff 
BuildRequires:    R-CRAN-bmp 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-imager 
BuildRequires:    R-CRAN-dplR 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-measuRing 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinyWidgets 
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-png 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-tiff 
Requires:         R-CRAN-bmp 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-imager 
Requires:         R-CRAN-dplR 
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-measuRing 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinyWidgets 

%description
Use morphological image processing and edge detection algorithms to
automatically measure tree ring widths on digital images. Users can also
manually mark tree rings on species with complex anatomical structures.
The arcs of inner-rings and angles of successive inclined ring boundaries
are used to correct ring-width series. The package provides a Shiny-based
application, allowing R beginners to easily analyze tree ring images and
export ring-width series in standard file formats.

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
%doc %{rlibdir}/%{packname}/001.png
%doc %{rlibdir}/%{packname}/missing_pith.png
%doc %{rlibdir}/%{packname}/mtr_app
%doc %{rlibdir}/%{packname}/README-img001.png
%doc %{rlibdir}/%{packname}/README-img002.png
%doc %{rlibdir}/%{packname}/RingCorrection.png
%{rlibdir}/%{packname}/INDEX
