%global packname  sptemExp
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          Constrained Spatiotemporal Mixed Models for Exposure Estimation

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14
Requires:         R-core >= 2.14
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-CRAN-SpatioTemporal 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-limSolve 
BuildRequires:    R-CRAN-R2BayesX 
BuildRequires:    R-CRAN-BayesX 
BuildRequires:    R-CRAN-BayesXsrc 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-bcv 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-splines 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-automap 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-methods 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-deldir 
Requires:         R-CRAN-SpatioTemporal 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-limSolve 
Requires:         R-CRAN-R2BayesX 
Requires:         R-CRAN-BayesX 
Requires:         R-CRAN-BayesXsrc 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-bcv 
Requires:         R-CRAN-rgeos 
Requires:         R-splines 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-automap 

%description
The approach of constrained spatiotemporal mixed models is to make
reliable estimation of air pollutant concentrations at high spatiotemporal
resolution (Li, L., Zhang, J., Meng, X., Fang, Y., Ge, Y., Wang, J., Wang,
C., Wu, J., Kan, H. (2018) <doi.org/10.1016/j.rse.2018.09.001>; Li, L.,
Lurmann, F., Habre, R., Urman, R., Rappaport, E., Ritz, B., Chen, J.,
Gilliland, F., Wu, J., (2017) <doi:10.1021/acs.est.7b01864>). This package
is an extensive tool for this modeling approach with support of block
Kriging (Goovaerts, P. (1997)
<http://www.gbv.de/dms/goettingen/229148123.pdf>) and uses the PM2.5
modeling as examples. It provides the following functionality: (1)
Extraction of covariates from the satellite images such as GeoTiff and NC4
raster; (2) Generation of temporal basis functions to simulate the
seasonal trends in the study regions; (3) Generation of the regional
monthly or yearly means of air pollutant concentration; (4) Generation of
Thiessen polygons and spatial effect modeling; (5) Ensemble modeling for
spatiotemporal mixed models, supporting multi-core parallel computing; (6)
Integrated predictions with or without weights of the model's performance,
supporting multi-core parallel computing; (7) Constrained optimization to
interpolate the missing values; (8) Generation of the grid surfaces of air
pollutant concentration estimates at high resolution; (9) Block Kriging
for regional mean estimation at multiple scales.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
