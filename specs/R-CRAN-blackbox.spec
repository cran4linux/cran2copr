%global packname  blackbox
%global packver   1.1.32
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.32
Release:          3%{?dist}%{?buildtag}
Summary:          Black Box Optimization and Exploration of Parameter Space

License:          CeCILL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-spaMM >= 3.1.0
BuildRequires:    R-CRAN-geometry >= 0.3.6
BuildRequires:    R-CRAN-Rcpp >= 0.12.10
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-rcdd 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-spaMM >= 3.1.0
Requires:         R-CRAN-geometry >= 0.3.6
Requires:         R-CRAN-Rcpp >= 0.12.10
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-rcdd 
Requires:         R-CRAN-proxy 
Requires:         R-lattice 
Requires:         R-CRAN-nloptr 
Requires:         R-MASS 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-foreach 

%description
Performs prediction of a response function from simulated response values,
allowing black-box optimization of functions estimated with some error.
Includes a simple user interface for such applications, as well as more
specialized functions designed to be called by the Migraine software
(Rousset and Leblois, 2012 <doi:10.1093/molbev/MSR262>; Leblois et al.,
2014 <doi:10.1093/molbev/msu212>; and see URL). The latter functions are
used for prediction of likelihood surfaces and implied likelihood ratio
confidence intervals, and for exploration of predictor space of the
surface. Prediction of the response is based on ordinary Kriging (with
residual error) of the input. Estimation of smoothing parameters is
performed by generalized cross-validation.

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
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
