%global packname  MoTBFs
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Learning Hybrid Bayesian Networks using Mixtures of TruncatedBasis Functions

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-bnlearn 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggm 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-bnlearn 
Requires:         R-methods 
Requires:         R-CRAN-ggm 

%description
Learning, manipulation and evaluation of mixtures of truncated basis
functions (MoTBFs), which include mixtures of polynomials (MOPs) and
mixtures of truncated exponentials (MTEs). MoTBFs are a flexible framework
for modelling hybrid Bayesian networks (I. Pérez-Bernabé, A. Salmerón, H.
Langseth (2015) <doi:10.1007/978-3-319-20807-7_36>; H. Langseth, T.D.
Nielsen, I. Pérez-Bernabé, A. Salmerón (2014)
<doi:10.1016/j.ijar.2013.09.012>; I. Pérez-Bernabé, A. Fernández, R. Rumí,
A. Salmerón (2016) <doi:10.1007/s10618-015-0429-7>). The package provides
functionality for learning univariate, multivariate and conditional
densities, with the possibility of incorporating prior knowledge.
Structural learning of hybrid Bayesian networks is also provided. A set of
useful tools is provided, including plotting, printing and likelihood
evaluation. This package makes use of S3 objects, with two new classes
called 'motbf' and 'jointmotbf'.

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
