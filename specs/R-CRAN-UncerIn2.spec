%global packname  UncerIn2
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}
Summary:          Implements Models of Uncertainty into the InterpolationFunctions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-RandomFields 
BuildRequires:    R-CRAN-automap 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-geoR 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-utils 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-RandomFields 
Requires:         R-CRAN-automap 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-geoR 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-Rcpp 
Requires:         R-utils 

%description
Provides a basic (random) data, grids, 6 models of uncertainty, 3
automatic interpolations (idw, spline, kriging), variogram and basic data
visualization.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
