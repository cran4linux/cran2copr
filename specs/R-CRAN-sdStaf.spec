%global packname  sdStaf
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}
Summary:          Species Distribution and Stability Future Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-rasterVis 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-dismo 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-rasterVis 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-dismo 

%description
Functions for post processing the outcomes of ecological niche models. It
further include methods to build stability maps based on species
distribution models under climate change projections and to reduce
environmental data.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/fut
%doc %{rlibdir}/%{packname}/pre
%{rlibdir}/%{packname}/INDEX
