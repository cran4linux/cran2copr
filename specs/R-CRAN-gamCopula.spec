%global packname  gamCopula
%global packver   0.0-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.7
Release:          2%{?dist}
Summary:          Generalized Additive Models for Bivariate Conditional DependenceStructures and Vine Copulas

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-VineCopula >= 2.0.0
BuildRequires:    R-CRAN-igraph >= 1.0.0
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-mgcv 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-VineCopula >= 2.0.0
Requires:         R-CRAN-igraph >= 1.0.0
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-mgcv 
Requires:         R-MASS 
Requires:         R-CRAN-gsl 
Requires:         R-CRAN-numDeriv 
Requires:         R-methods 
Requires:         R-CRAN-copula 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 

%description
Implementation of various inference and simulation tools to apply
generalized additive models to bivariate dependence structures and
non-simplified vine copulas.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
