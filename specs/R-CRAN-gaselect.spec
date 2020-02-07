%global packname  gaselect
%global packver   1.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.9
Release:          1%{?dist}
Summary:          Genetic Algorithm (GA) for Variable Selection fromHigh-Dimensional Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-methods >= 2.10.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.4.000
BuildRequires:    R-CRAN-Rcpp >= 0.10.5
Requires:         R-methods >= 2.10.0
Requires:         R-CRAN-Rcpp >= 0.10.5

%description
Provides a genetic algorithm for finding variable subsets in high
dimensional data with high prediction performance. The genetic algorithm
can use ordinary least squares (OLS) regression models or partial least
squares (PLS) regression models to evaluate the prediction power of
variable subsets. By supporting different cross-validation schemes, the
user can fine-tune the tradeoff between speed and quality of the solution.

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
%{rlibdir}/%{packname}/libs
