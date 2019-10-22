%global packname  Directional
%global packver   4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0
Release:          1%{?dist}
Summary:          Directional Statistics

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-bigstatsr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-Rfast2 
BuildRequires:    R-CRAN-RcppZiggurat 
BuildRequires:    R-CRAN-rgl 
Requires:         R-CRAN-bigstatsr 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-MASS 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-Rfast2 
Requires:         R-CRAN-RcppZiggurat 
Requires:         R-CRAN-rgl 

%description
A collection of functions for directional data (including massive, with
millions of observations, data) analysis. Hypothesis testing, discriminant
and regression analysis, MLE of distributions and more are included. The
standard textbook for such data is the "Directional Statistics" by Mardia,
K. V. and Jupp, P. E. (2000). Other references include Phillip J. Paine,
Simon P. Preston Michail Tsagris and Andrew T. A. Wood (2018). An
elliptically symmetric angular Gaussian distribution. Statistics and
Computing 28(3): 689-697. <doi:10.1007/s11222-017-9756-4>, P. J. Paine, S.
P. Preston, M. Tsagris and Andrew T. A. Wood (2019). Spherical regression
models with general covariates and anisotropic errors. Statistics and
Computing (to appear). <doi:10.1007/s11222-019-09872-2>.

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
%{rlibdir}/%{packname}/INDEX
