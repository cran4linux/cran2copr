%global packname  move
%global packver   4.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0.0
Release:          2%{?dist}
Summary:          Visualizing and Analyzing Animal Track Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-raster >= 2.4.15
BuildRequires:    R-CRAN-geosphere >= 1.4.3
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-raster >= 2.4.15
Requires:         R-CRAN-geosphere >= 1.4.3
Requires:         R-methods 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-Rcpp 

%description
Contains functions to access movement data stored in 'movebank.org' as
well as tools to visualize and statistically analyze animal movement data,
among others functions to calculate dynamic Brownian Bridge Movement
Models. Move helps addressing movement ecology questions.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
