%global packname  GCPM
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          2%{?dist}
Summary:          Generalized Credit Portfolio Model

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
BuildRequires:    R-CRAN-RcppProgress >= 0.1
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
Requires:         R-CRAN-Rcpp >= 0.11.2
Requires:         R-CRAN-RcppProgress >= 0.1
Requires:         R-methods 
Requires:         R-parallel 

%description
Analyze the default risk of credit portfolios. Commonly known models, like
CreditRisk+ or the CreditMetrics model are implemented in their very basic
settings. The portfolio loss distribution can be achieved either by
simulation or analytically in case of the classic CreditRisk+ model.
Models are only implemented to respect losses caused by defaults, i.e.
migration risk is not included. The package structure is kept flexible
especially with respect to distributional assumptions in order to quantify
the sensitivity of risk figures with respect to several assumptions.
Therefore the package can be used to determine the credit risk of a given
portfolio as well as to quantify model sensitivities.

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
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
