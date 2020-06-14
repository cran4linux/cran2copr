%global packname  jmcm
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          2%{?dist}
Summary:          Joint Mean-Covariance Models using 'Armadillo' and S4

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.14
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-lattice 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-roptim 
Requires:         R-CRAN-Rcpp >= 0.12.14
Requires:         R-CRAN-Formula 
Requires:         R-lattice 
Requires:         R-methods 

%description
Fit joint mean-covariance models for longitudinal data. The models and
their components are represented using S4 classes and methods. The core
computational algorithms are implemented using the 'Armadillo' C++ library
for numerical linear algebra and 'RcppArmadillo' glue.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
