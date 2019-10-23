%global packname  varbvs
%global packver   2.5-16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5.16
Release:          1%{?dist}
Summary:          Large-Scale Bayesian Variable Selection Using VariationalMethods

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-methods 
BuildRequires:    R-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-nor1mix 
Requires:         R-methods 
Requires:         R-Matrix 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-lattice 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-nor1mix 

%description
Fast algorithms for fitting Bayesian variable selection models and
computing Bayes factors, in which the outcome (or response variable) is
modeled using a linear regression or a logistic regression. The algorithms
are based on the variational approximations described in "Scalable
variational inference for Bayesian variable selection in regression, and
its accuracy in genetic association studies" (P. Carbonetto & M. Stephens,
2012, <DOI:10.1214/12-BA703>). This software has been applied to large
data sets with over a million variables and thousands of samples.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/code
%{rlibdir}/%{packname}/datafiles
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
