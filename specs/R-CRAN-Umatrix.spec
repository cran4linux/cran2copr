%global __brp_check_rpaths %{nil}
%global packname  Umatrix
%global packver   3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3
Release:          3%{?dist}%{?buildtag}
Summary:          Visualization of Structures in High-Dimensional Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-tools 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-pdist 
BuildRequires:    R-CRAN-AdaptGauss 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-png 
Requires:         R-tools 
Requires:         R-grid 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-deldir 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-pdist 
Requires:         R-CRAN-AdaptGauss 
Requires:         R-CRAN-pracma 

%description
By gaining the property of emergence through self-organization, the
enhancement of SOMs(self organizing maps) is called Emergent SOM (ESOM).
The result of the projection by ESOM is a grid of neurons which can be
visualised as a three dimensional landscape in form of the Umatrix.
Further details can be found in the referenced publications (see url).
This package offers tools for calculating and visualising the ESOM as well
as Umatrix, Pmatrix and UStarMatrix. All the functionality is also
available through graphical user interfaces implemented in 'shiny'.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
