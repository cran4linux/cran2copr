%global packname  DepthProc
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}
Summary:          Statistical Depth Functions for Multivariate Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-methods 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-np 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-sm 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.11.2
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rrcov 
Requires:         R-methods 
Requires:         R-MASS 
Requires:         R-CRAN-np 
Requires:         R-lattice 
Requires:         R-CRAN-sm 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-zoo 
Requires:         R-grDevices 

%description
Data depth concept offers a variety of powerful and user friendly tools
for robust exploration and inference for multivariate data. The offered
techniques may be successfully used in cases of lack of our knowledge on
parametric models generating data due to their nature. The package consist
of among others implementations of several data depth techniques involving
multivariate quantile-quantile plots, multivariate scatter estimators,
multivariate Wilcoxon tests and robust regressions.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
