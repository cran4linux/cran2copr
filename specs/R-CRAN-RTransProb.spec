%global packname  RTransProb
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}
Summary:          Analyze and Forecast Credit Migrations

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.2.0
Requires:         R-core >= 2.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.11
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-neuralnet 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.11
Requires:         R-CRAN-chron 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-expm 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-neuralnet 
Requires:         R-nnet 
Requires:         R-CRAN-pracma 
Requires:         R-tcltk 
Requires:         R-CRAN-zoo 

%description
A set of functions used to automate commonly used methods in credit risk
to estimate migration (transition) matrices. The package includes multiple
methods for bootstrapping default rates and forecasting/stress testing
credit exposures migrations, via Econometric and Machine Learning
approaches.  More information can be found at
<https://analyticsrusers.blog>.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
