%global packname  glmaag
%global packver   0.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.6
Release:          3%{?dist}
Summary:          Adaptive LASSO and Network Regularized Generalized Linear Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-maxstat 
BuildRequires:    R-CRAN-survminer 
BuildRequires:    R-CRAN-plotROC 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-huge 
BuildRequires:    R-CRAN-OptimalCutpoints 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-survival 
Requires:         R-CRAN-data.table 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-Matrix 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-maxstat 
Requires:         R-CRAN-survminer 
Requires:         R-CRAN-plotROC 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-huge 
Requires:         R-CRAN-OptimalCutpoints 

%description
Efficient procedures for adaptive LASSO and network regularized for
Gaussian, logistic, and Cox model. Provides network estimation procedure
(combination of methods proposed by Ucar, et. al (2007)
<doi:10.1093/bioinformatics/btm423> and Meinshausen and Buhlmann (2006)
<doi:10.1214/009053606000000281>), cross validation and stability
selection proposed by Meinshausen and Buhlmann (2010)
<doi:10.1111/j.1467-9868.2010.00740.x> and Liu, Roeder and Wasserman
(2010) <arXiv:1006.3316> methods. Interactive R app is available.

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
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/shiny_examples
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
