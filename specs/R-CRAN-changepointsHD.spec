%global packname  changepointsHD
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}
Summary:          Change-Point Estimation for Expensive and High-DimensionalModels

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-methods 

%description
This implements the methods developed in, L. Bybee and Y. Atchade. (2018).
Contains a series of methods for estimating change-points given user
specified black-box models.  The methods include binary segmentation for
multiple change-point estimation. For estimating each individual
change-point the package includes simulated annealing, brute force, and,
for Gaussian graphical models, an applications specific rank-one update
implementation.  Additionally, code for estimating Gaussian graphical
models is included.  The goal of this package is to allow for the
efficient estimation of change-points in complicated models with high
dimensional data.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
