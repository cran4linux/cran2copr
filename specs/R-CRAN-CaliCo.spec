%global packname  CaliCo
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Code Calibration in a Bayesian Framework

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-DiceKriging 
BuildRequires:    R-CRAN-DiceDesign 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-DiceKriging 
Requires:         R-CRAN-DiceDesign 
Requires:         R-MASS 
Requires:         R-CRAN-coda 
Requires:         R-parallel 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-gtools 

%description
Calibration of every computational code. It uses a Bayesian framework to
rule the estimation. With a new data set, the prediction will create a
prevision set taking into account the new calibrated parameters. The
choices between several models is also available. The methods are
described in the paper Carmassi et al. (2018) <arXiv:1801.01810>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
