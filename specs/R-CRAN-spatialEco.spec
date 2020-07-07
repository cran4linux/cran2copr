%global packname  spatialEco
%global packver   1.3-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          3%{?dist}
Summary:          Spatial Analysis and Modelling Utilities

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-rgeos 
Requires:         R-MASS 
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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
