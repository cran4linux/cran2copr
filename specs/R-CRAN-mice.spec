%global packname  mice
%global packver   3.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.7.0
Release:          1%{?dist}
Summary:          Multivariate Imputation by Chained Equations

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-methods 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mitml 
BuildRequires:    R-nnet 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-rpart 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-survival 
BuildRequires:    R-utils 
Requires:         R-methods 
Requires:         R-lattice 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-dplyr 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-MASS 
Requires:         R-CRAN-mitml 
Requires:         R-nnet 
Requires:         R-parallel 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rlang 
Requires:         R-rpart 
Requires:         R-splines 
Requires:         R-stats 
Requires:         R-survival 
Requires:         R-utils 

%description
Multiple imputation using Fully Conditional Specification (FCS)
implemented by the MICE algorithm as described in Van Buuren and
Groothuis-Oudshoorn (2011) <doi:10.18637/jss.v045.i03>. Each variable has
its own imputation model. Built-in imputation models are provided for
continuous data (predictive mean matching, normal), binary data (logistic
regression), unordered categorical data (polytomous logistic regression)
and ordered categorical data (proportional odds). MICE can also impute
continuous two-level data (normal model, pan, second-level variables).
Passive imputation can be used to maintain consistency between variables.
Various diagnostic plots are available to inspect the quality of the
imputations.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
