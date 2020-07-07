%global packname  TAG
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}
Summary:          Transformed Additive Gaussian Processes

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-DiceKriging 
BuildRequires:    R-Matrix 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-FastGP 
BuildRequires:    R-CRAN-mlegp 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-DiceKriging 
Requires:         R-Matrix 
Requires:         R-mgcv 
Requires:         R-CRAN-FastGP 
Requires:         R-CRAN-mlegp 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-doParallel 

%description
Implement the transformed additive Gaussian (TAG) process and the
transformed approximately additive Gaussian (TAAG) process proposed in Lin
and Joseph (2019+) <DOI:10.1080/00401706.2019.1665592>. These functions
can be used to model deterministic computer experiments, obtain
predictions at new inputs, and quantify the uncertainty of the
predictions.

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
