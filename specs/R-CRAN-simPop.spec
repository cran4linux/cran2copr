%global packname  simPop
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          3%{?dist}
Summary:          Simulation of Synthetic Populations for Survey Data ConsideringAuxiliary Information

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-vcd 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-laeken 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-parallel 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-VIM 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-party 
BuildRequires:    R-CRAN-EnvStats 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-wrswoR 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-lattice 
Requires:         R-CRAN-vcd 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-laeken 
Requires:         R-CRAN-plyr 
Requires:         R-MASS 
Requires:         R-CRAN-RcppArmadillo 
Requires:         R-CRAN-e1071 
Requires:         R-parallel 
Requires:         R-nnet 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-VIM 
Requires:         R-methods 
Requires:         R-CRAN-party 
Requires:         R-CRAN-EnvStats 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-wrswoR 

%description
Tools and methods to simulate populations for surveys based on auxiliary
data. The tools include model-based methods, calibration and combinatorial
optimization algorithms. The package was developed with support of the
International Household Survey Network, DFID Trust Fund TF011722 and funds
from the World bank.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
