%global packname  landsepi
%global packver   0.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.8
Release:          1%{?dist}
Summary:          Landscape Epidemiology and Evolution

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel
BuildRequires:    gdal-devel >= 1.11.0
Requires:         gsl
Requires:         gdal
BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-stats >= 3.0.2
BuildRequires:    R-grDevices >= 3.0.0
BuildRequires:    R-graphics >= 3.0.0
BuildRequires:    R-CRAN-rgdal >= 1.2.16
BuildRequires:    R-CRAN-sp >= 1.0.17
BuildRequires:    R-CRAN-Rcpp >= 0.9.0
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-Matrix 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-splancs 
BuildRequires:    R-CRAN-sf 
Requires:         R-stats >= 3.0.2
Requires:         R-grDevices >= 3.0.0
Requires:         R-graphics >= 3.0.0
Requires:         R-CRAN-rgdal >= 1.2.16
Requires:         R-CRAN-sp >= 1.0.17
Requires:         R-CRAN-Rcpp >= 0.9.0
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-Matrix 
Requires:         R-MASS 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-splancs 
Requires:         R-CRAN-sf 

%description
A spatio-temporal stochastic model to assess resistance deployment
strategies against plant pathogens. The model is based on stochastic
geometry for describing the landscape and the resistant hosts, a dispersal
kernel for the dissemination of the pathogen, and a SEIR
(Susceptible-Exposed-Infectious-Removed) architecture to simulate plant
response to disease. Loup Rimbaud, Julien Papaïx, Jean-François Rey, Luke
G Barrett, Peter H Thrall (2018) <doi:10.1371/journal.pcbi.1006067>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
