%global __brp_check_rpaths %{nil}
%global debug_package %{nil}
%global packname  beam
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Fast Bayesian Inference in Large Gaussian Graphical Models

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-fdrtool 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-BH 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-Matrix 
Requires:         R-CRAN-fdrtool 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-assertthat 

%description
Fast Bayesian inference of marginal and conditional independence
structures from high-dimensional data. Leday and Richardson (2019),
Biometrics, <doi:10.1111/biom.13064>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
