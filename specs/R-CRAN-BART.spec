%global packname  BART
%global packver   2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.6
Release:          1%{?dist}
Summary:          Bayesian Additive Regression Trees

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-nlme 
BuildRequires:    R-nnet 
BuildRequires:    R-survival 
BuildRequires:    R-parallel 
BuildRequires:    R-tools 
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-nlme 
Requires:         R-nnet 
Requires:         R-survival 
Requires:         R-parallel 
Requires:         R-tools 

%description
Bayesian Additive Regression Trees (BART) provide flexible nonparametric
modeling of covariates for continuous, binary, categorical and
time-to-event outcomes.  For more information on BART, see Chipman, George
and McCulloch (2010) <doi:10.1214/09-AOAS285> and Sparapani, Logan,
McCulloch and Laud (2016) <doi:10.1002/sim.6893>.

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
%doc %{rlibdir}/%{packname}/cxx-ex
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
