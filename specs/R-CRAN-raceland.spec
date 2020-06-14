%global packname  raceland
%global packver   1.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          2%{?dist}
Summary:          Pattern-Based Zoneless Method for Analysis and Visualization ofRacial Topography

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-comat >= 0.7.0
BuildRequires:    R-CRAN-fasterize 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plotwidgets 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-fasterize 
Requires:         R-methods 
Requires:         R-CRAN-plotwidgets 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-comat >= 0.7.0

%description
Implements a computational framework for a pattern-based, zoneless
analysis, and visualization of (ethno)racial topography. It is a
reimagined approach for analyzing residential segregation and racial
diversity based on the concept of 'landscape’ used in the domain of
landscape ecology.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/rast_data
%doc %{rlibdir}/%{packname}/results
%{rlibdir}/%{packname}/vect_data
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
