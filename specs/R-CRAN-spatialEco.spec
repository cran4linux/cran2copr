%global packname  spatialEco
%global packver   1.2-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Spatial Analysis and Modelling Utilities

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-SpatialPack >= 0.3
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-SDMTools 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-yaImpute 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-EnvStats 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-methods 
Requires:         R-CRAN-SpatialPack >= 0.3
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-spatstat 
Requires:         R-cluster 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-SDMTools 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-yaImpute 
Requires:         R-MASS 
Requires:         R-CRAN-EnvStats 
Requires:         R-CRAN-maptools 
Requires:         R-methods 

%description
Utilities to support spatial data manipulation, query, sampling and
modelling. Functions include models for species population density,
download utilities for climate and global deforestation spatial products,
spatial smoothing, multivariate separability, point process model for
creating pseudo- absences and sub-sampling, polygon and point-distance
landscape metrics, auto-logistic model, sampling models, cluster
optimization, statistical exploratory tools and raster-based metrics.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
