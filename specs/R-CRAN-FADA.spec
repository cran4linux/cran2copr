%global packname  FADA
%global packver   1.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.5
Release:          1%{?dist}
Summary:          Variable Selection for Supervised Classification in HighDimension

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-elasticnet 
BuildRequires:    R-CRAN-sparseLDA 
BuildRequires:    R-CRAN-sda 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-crossval 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-methods 
Requires:         R-MASS 
Requires:         R-CRAN-elasticnet 
Requires:         R-CRAN-sparseLDA 
Requires:         R-CRAN-sda 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-crossval 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-matrixStats 
Requires:         R-methods 

%description
The functions provided in the FADA (Factor Adjusted Discriminant Analysis)
package aim at performing supervised classification of high-dimensional
and correlated profiles. The procedure combines a decorrelation step based
on a factor modeling of the dependence among covariates and a
classification method. The available methods are Lasso regularized
logistic model (see Friedman et al. (2010)), sparse linear discriminant
analysis (see Clemmensen et al. (2011)), shrinkage linear and diagonal
discriminant analysis (see M. Ahdesmaki et al. (2010)). More methods of
classification can be used on the decorrelated data provided by the
package FADA.

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
