%global packname  SpaDES.tools
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}
Summary:          Additional Tools for Developing Spatially Explicit DiscreteEvent Simulation (SpaDES) Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-raster >= 2.5.8
BuildRequires:    R-CRAN-ff >= 2.2.13
BuildRequires:    R-CRAN-checkmate >= 1.8.2
BuildRequires:    R-CRAN-sp >= 1.2.4
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-CRAN-bit >= 1.1.12
BuildRequires:    R-CRAN-fastmatch >= 1.1.0
BuildRequires:    R-CRAN-CircStats >= 0.2.4
BuildRequires:    R-CRAN-fpCompare >= 0.2.1
BuildRequires:    R-CRAN-reproducible >= 0.2.0
BuildRequires:    R-CRAN-ffbase >= 0.12.3
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-quickPlot 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-stats 
Requires:         R-CRAN-raster >= 2.5.8
Requires:         R-CRAN-ff >= 2.2.13
Requires:         R-CRAN-checkmate >= 1.8.2
Requires:         R-CRAN-sp >= 1.2.4
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-CRAN-bit >= 1.1.12
Requires:         R-CRAN-fastmatch >= 1.1.0
Requires:         R-CRAN-CircStats >= 0.2.4
Requires:         R-CRAN-fpCompare >= 0.2.1
Requires:         R-CRAN-reproducible >= 0.2.0
Requires:         R-CRAN-ffbase >= 0.12.3
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-quickPlot 
Requires:         R-CRAN-rgeos 
Requires:         R-stats 

%description
Provides GIS and map utilities, plus additional modeling tools for
developing cellular automata, dynamic raster models, and agent based
models in 'SpaDES'. Included are various methods for spatial spreading,
spatial agents, GIS operations, random map generation, and others. See
'?SpaDES.tools' for an categorized overview of these additional tools.

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
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
