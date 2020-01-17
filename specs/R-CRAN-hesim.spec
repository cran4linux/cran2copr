%global packname  hesim
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}
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
Parameterize, simulate, and analyze health-economic simulation models.
Supports N-state partitioned survival models (Glasziou et al. 1990)
<doi:10.1002/sim.4780091106> and continuous time state transition models
(Siebert et al. 2012) <doi:10.1016/j.jval.2012.06.014> parameterized using
survival or multi-state modeling (de Wreede et al. 2011, Jackson 2015)
<doi:10.18637/jss.v038.i07>, <doi:10.18637/jss.v070.i08>. Decision
uncertainty from a cost-effectiveness analysis is quantified with standard
graphical and tabular summaries of a probabilistic sensitivity analysis
(Claxton et al. 2005, Barton et al. 2008) <doi:10.1002/hec.985>,
<doi:10.1111/j.1524-4733.2008.00358.x>. Simulation code written in C++ to
boost performance.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
