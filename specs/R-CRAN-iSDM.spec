%global packname  iSDM
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Invasive Species Distribution Modelling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-pdist 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-colorRamps 
BuildRequires:    R-CRAN-virtualspecies 
BuildRequires:    R-CRAN-rgl 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-maptools 
Requires:         R-MASS 
Requires:         R-CRAN-pdist 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-colorRamps 
Requires:         R-CRAN-virtualspecies 
Requires:         R-CRAN-rgl 

%description
Functions for predicting and mapping potential and realized distributions
of invasive species within the invaded range.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
