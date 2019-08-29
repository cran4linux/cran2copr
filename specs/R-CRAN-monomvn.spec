%global packname  monomvn
%global packver   1.9-10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.10
Release:          1%{?dist}
Summary:          Estimation for Multivariate Normal and Student-t Data withMonotone Missingness

License:          LGPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-lars 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-lars 
Requires:         R-MASS 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-mvtnorm 

%description
Estimation of multivariate normal and student-t data of arbitrary
dimension where the pattern of missing data is monotone. Through the use
of parsimonious/shrinkage regressions (plsr, pcr, lasso, ridge, etc.),
where standard regressions fail, the package can handle a nearly arbitrary
amount of missing data. The current version supports maximum likelihood
inference and a full Bayesian approach employing scale-mixtures for Gibbs
sampling. Monotone data augmentation extends this Bayesian approach to
arbitrary missingness patterns.  A fully functional standalone interface
to the Bayesian lasso (from Park & Casella), Normal-Gamma (from Griffin &
Brown), Horseshoe (from Carvalho, Polson, & Scott), and ridge regression
with model selection via Reversible Jump, and student-t errors (from
Geweke) is also provided.

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
