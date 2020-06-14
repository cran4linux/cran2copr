%global packname  hesim
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          2%{?dist}
Summary:          Health-Economic Simulation Modeling and Decision Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.16
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-flexsurv 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-stats 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.16
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-flexsurv 
Requires:         R-MASS 
Requires:         R-CRAN-R6 
Requires:         R-stats 
Requires:         R-survival 

%description
A modular and computationally efficient R package for parameterizing,
simulating, and analyzing health-economic simulation models. The package
supports cohort discrete time state transition models (Briggs et al. 1998)
<doi:10.2165/00019053-199813040-00003>, N-state partitioned survival
models (Glasziou et al. 1990) <doi:10.1002/sim.4780091106>, and
individual-level continuous time state transition models (Siebert et al.
2012) <doi:10.1016/j.jval.2012.06.014>, encompassing both Markov
(time-homogeneous and time-inhomogeneous) and semi-Markov processes.
Decision uncertainty from a cost-effectiveness analysis is quantified with
standard graphical and tabular summaries of a probabilistic sensitivity
analysis (Claxton et al. 2005, Barton et al. 2008) <doi:10.1002/hec.985>,
<doi:10.1111/j.1524-4733.2008.00358.x>. Use of C++ and data.table make
individual-patient simulation, probabilistic sensitivity analysis, and
incorporation of patient heterogeneity fast.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
