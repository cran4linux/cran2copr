%global packname  FRK
%global packver   0.2.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2.1
Release:          1%{?dist}
Summary:          Fixed Rank Kriging

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-Hmisc >= 4.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spacetime 
BuildRequires:    R-CRAN-sparseinv 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-Hmisc >= 4.1
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-digest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spacetime 
Requires:         R-CRAN-sparseinv 
Requires:         R-stats 
Requires:         R-utils 

%description
Fixed Rank Kriging is a tool for spatial/spatio-temporal modelling and
prediction with large datasets. The approach, discussed in Cressie and
Johannesson (2008) <DOI:10.1111/j.1467-9868.2007.00633.x>, decomposes the
field, and hence the covariance function, using a fixed set of n basis
functions, where n is typically much smaller than the number of data
points (or polygons) m. The method naturally allows for non-stationary,
anisotropic covariance functions and the use of observations with varying
support (with known error variance). The projected field is a key building
block of the Spatial Random Effects (SRE) model, on which this package is
based. The package FRK provides helper functions to model, fit, and
predict using an SRE with relative ease.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
