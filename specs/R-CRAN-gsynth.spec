%global packname  gsynth
%global packver   1.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.9
Release:          3%{?dist}%{?buildtag}
Summary:          Generalized Synthetic Control Method

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-MASS >= 7.3.47
BuildRequires:    R-CRAN-ggplot2 >= 2.1.0
BuildRequires:    R-CRAN-foreach >= 1.4.3
BuildRequires:    R-CRAN-abind >= 1.4.0
BuildRequires:    R-CRAN-mvtnorm >= 1.0.6
BuildRequires:    R-CRAN-doParallel >= 1.0.10
BuildRequires:    R-CRAN-GGally >= 1.0.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-MASS >= 7.3.47
Requires:         R-CRAN-ggplot2 >= 2.1.0
Requires:         R-CRAN-foreach >= 1.4.3
Requires:         R-CRAN-abind >= 1.4.0
Requires:         R-CRAN-mvtnorm >= 1.0.6
Requires:         R-CRAN-doParallel >= 1.0.10
Requires:         R-CRAN-GGally >= 1.0.1
Requires:         R-CRAN-Rcpp >= 0.12.3

%description
Provides causal inference with interactive fixed-effect models. It imputes
counterfactuals for each treated unit using control group information
based on a linear interactive fixed effects model that incorporates
unit-specific intercepts interacted with time-varying coefficients. This
method generalizes the synthetic control method to the case of multiple
treated units and variable treatment periods, and improves efficiency and
interpretability. This version supports unbalanced panels and implements
the matrix completion method. Main reference: Yiqing Xu (2017)
<doi:10.1017/pan.2016.2>.

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
