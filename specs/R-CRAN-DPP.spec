%global packname  DPP
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Inference of Parameters of Normal Distributions from a Mixtureof Normals

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.4
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 0.12.4
Requires:         R-methods 
Requires:         R-CRAN-coda 
Requires:         R-stats 

%description
This MCMC method takes a data numeric vector (Y) and assigns the elements
of Y to a (potentially infinite) number of normal distributions. The
individual normal distributions from a mixture of normals can be inferred.
Following the method described in Escobar (1994) <doi:10.2307/2291223> we
use a Dirichlet Process Prior (DPP) to describe stochastically our prior
assumptions about the dimensionality of the data.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
