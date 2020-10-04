%global packname  BayesESS
%global packver   0.1.19
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.19
Release:          3%{?dist}%{?buildtag}
Summary:          Determining Effective Sample Size

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-dfcrm 
BuildRequires:    R-CRAN-MatrixModels 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-MCMCpack 
Requires:         R-stats 
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-dfcrm 
Requires:         R-CRAN-MatrixModels 
Requires:         R-MASS 

%description
Determines effective sample size of a parametric prior distribution in
Bayesian models. For a web-based Shiny application related to this
package, see <https://implement.shinyapps.io/bayesess/>.

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
