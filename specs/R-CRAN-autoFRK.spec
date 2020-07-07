%global packname  autoFRK
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          3%{?dist}
Summary:          Automatic Fixed Rank Kriging

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-fields >= 6.9
BuildRequires:    R-CRAN-LatticeKrig >= 5.4
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-CRAN-filehashSQLite 
BuildRequires:    R-CRAN-filehash 
BuildRequires:    R-MASS 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-filematrix 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-RcppParallel 
Requires:         R-CRAN-fields >= 6.9
Requires:         R-CRAN-LatticeKrig >= 5.4
Requires:         R-CRAN-spam 
Requires:         R-CRAN-filehashSQLite 
Requires:         R-CRAN-filehash 
Requires:         R-MASS 
Requires:         R-mgcv 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-filematrix 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 

%description
Automatic fixed rank kriging for (irregularly located) spatial data using
a class of basis functions with multi-resolution features and ordered in
terms of their resolutions. The model parameters are estimated by maximum
likelihood (ML) and the number of basis functions is determined by
Akaike's information criterion (AIC). For spatial data with either one
realization or independent replicates, the ML estimates and AIC are
efficiently computed using their closed-form expressions when no missing
value occurs. Details regarding the basis function construction, parameter
estimation, and AIC calculation can be found in Tzeng and Huang (2018)
<doi:10.1080/00401706.2017.1345701>. For data with missing values, the ML
estimates are obtained using the expectation- maximization algorithm.
Apart from the number of basis functions, there are no other tuning
parameters, making the method fully automatic. Users can also include a
stationary structure in the spatial covariance, which utilizes
'LatticeKrig' package.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
