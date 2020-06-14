%global packname  mobsim
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Spatial Simulation and Scale-Dependent Analysis of BiodiversityChanges

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-sads >= 0.4.1
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-sads >= 0.4.1
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-vegan 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-stats 

%description
Tools for the simulation, analysis and sampling of spatial biodiversity
data (May et al. 2017) <doi:10.1101/209502>. In the simulation tools user
define the numbers of species and individuals, the species abundance
distribution and species aggregation. Functions for analysis include
species rarefaction and accumulation curves, species-area relationships
and the distance decay of similarity.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/image
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
