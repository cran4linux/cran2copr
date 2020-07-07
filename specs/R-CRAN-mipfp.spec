%global packname  mipfp
%global packver   3.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.1
Release:          3%{?dist}
Summary:          Multidimensional Iterative Proportional Fitting and AlternativeModels

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cmm 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-cmm 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-numDeriv 

%description
An implementation of the iterative proportional fitting (IPFP), maximum
likelihood, minimum chi-square and weighted least squares procedures for
updating a N-dimensional array with respect to given target marginal
distributions (which, in turn can be multidimensional). The package also
provides an application of the IPFP to simulate multivariate Bernoulli
distributions.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
