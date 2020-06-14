%global packname  adespatial
%global packver   0.3-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.8
Release:          2%{?dist}
Summary:          Multivariate Multiscale Spatial Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ade4 >= 1.7.13
BuildRequires:    R-CRAN-adegraphics 
BuildRequires:    R-CRAN-adephylo 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-lattice 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-ade4 >= 1.7.13
Requires:         R-CRAN-adegraphics 
Requires:         R-CRAN-adephylo 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spdep 
Requires:         R-lattice 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-vegan 

%description
Tools for the multiscale spatial analysis of multivariate data. Several
methods are based on the use of a spatial weighting matrix and its
eigenvector decomposition (Moran's Eigenvectors Maps, MEM). Several
approaches are described in the review Dray et al (2012)
<doi:10.1890/11-1183.1>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/listw.explore
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
