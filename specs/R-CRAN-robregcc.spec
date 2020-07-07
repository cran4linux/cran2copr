%global packname  robregcc
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Robust Regression with Compositional Covariates

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-MASS 
Requires:         R-CRAN-magrittr 
Requires:         R-graphics 

%description
We implement the algorithm estimating the parameters of the robust
regression model with compositional covariates. The model simultaneously
treats outliers and provides reliable parameter estimates. Publication
reference: Mishra, A., Mueller, C.,(2019) <arXiv:1909.04990>.

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
