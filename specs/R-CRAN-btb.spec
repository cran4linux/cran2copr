%global packname  btb
%global packver   0.1.30
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.30
Release:          1%{?dist}
Summary:          Beyond the Border - Kernel Density Estimation for UrbanGeography

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-BH >= 1.60.0.1
BuildRequires:    R-CRAN-Rcpp >= 0.11.3
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.11.3
Requires:         R-methods 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-RcppParallel 

%description
The kernelSmoothing() function allows you to square and smooth geolocated
data. It calculates a classical kernel smoothing (conservative) or a
geographically weighted median. There are four major call modes of the
function. The first call mode is kernelSmoothing(obs, epsg, cellsize,
bandwith) for a classical kernel smoothing and automatic grid. The second
call mode is kernelSmoothing(obs, epsg, cellsize, bandwith, quantiles) for
a geographically weighted median and automatic grid. The third call mode
is kernelSmoothing(obs, epsg, cellsize, bandwith, centroids) for a
classical kernel smoothing and user grid. The fourth call mode is
kernelSmoothing(obs, epsg, cellsize, bandwith, quantiles, centroids) for a
geographically weighted median and user grid. Geographically weighted
summary statistics : a framework for localised exploratory data analysis,
C.Brunsdon & al., in Computers, Environment and Urban Systems C.Brunsdon &
al. (2002) <doi:10.1016/S0198-9715(01)00009-6>, Statistical Analysis of
Spatial and Spatio-Temporal Point Patterns, Third Edition, Diggle, pp.
83-86, (2003) <doi:10.1080/13658816.2014.937718>.

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
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/testsUnitaires
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
