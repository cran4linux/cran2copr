%global packname  CorReg
%global packver   1.2.17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.17
Release:          3%{?dist}
Summary:          Linear Regression Based on Linear Structure Between Variables

License:          CeCILL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-MASS >= 7.3.30
BuildRequires:    R-CRAN-mclust >= 4.2
BuildRequires:    R-rpart >= 4.1.5
BuildRequires:    R-CRAN-glmnet >= 2.0.2
BuildRequires:    R-CRAN-lars >= 1.2
BuildRequires:    R-CRAN-elasticnet >= 1.1
BuildRequires:    R-Matrix >= 1.1
BuildRequires:    R-CRAN-mvtnorm >= 0.9
BuildRequires:    R-CRAN-corrplot >= 0.73
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-MASS >= 7.3.30
Requires:         R-CRAN-mclust >= 4.2
Requires:         R-rpart >= 4.1.5
Requires:         R-CRAN-glmnet >= 2.0.2
Requires:         R-CRAN-lars >= 1.2
Requires:         R-CRAN-elasticnet >= 1.1
Requires:         R-Matrix >= 1.1
Requires:         R-CRAN-mvtnorm >= 0.9
Requires:         R-CRAN-corrplot >= 0.73
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-methods 

%description
Linear regression based on a recursive structural equation model (explicit
multiples correlations) found by a M.C.M.C.(Markov Chain Monte Carlo)
algorithm. It permits to face highly correlated variables. Variable
selection is included (by lasso, elastic net, etc.). It also provides some
graphical tools for basic statistics. For more information about the
method, read the PhD thesis of Clement Thery (2015) in the link below.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
