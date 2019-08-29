%global packname  FDGcopulas
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Multivariate Dependence with FDG Copulas

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.10.6
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-randtoolbox 
Requires:         R-CRAN-Rcpp >= 0.10.6
Requires:         R-methods 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-randtoolbox 

%description
FDG copulas are a class of copulas featuring an interesting balance
between flexibility and tractability. This package provides tools to
construct, calculate the pairwise dependence coefficients of, simulate
from, and fit FDG copulas. The acronym FDG stands for 'one-Factor with
Durante Generators', as an FDG copula is a one-factor copula -- that is,
the variables are independent given a latent factor -- whose linking
copulas belong to the Durante class of bivariate copulas (also referred to
as exchangeable Marshall-Olkin or semilinear copulas).

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
