%global packname  eseis
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          2%{?dist}
Summary:          Environmental Seismology Toolbox

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.5
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-multitaper 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-fftw 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-IRISSeismic 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-reticulate 
Requires:         R-CRAN-Rcpp >= 0.12.5
Requires:         R-CRAN-sp 
Requires:         R-CRAN-multitaper 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-caTools 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-fftw 
Requires:         R-CRAN-matrixStats 
Requires:         R-methods 
Requires:         R-CRAN-IRISSeismic 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-reticulate 

%description
Environmental seismology is a scientific field that studies the seismic
signals, emitted by Earth surface processes. This package provides all
relevant functions to read/write seismic data files, prepare, analyse and
visualise seismic data, and generate reports of the processing history.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
