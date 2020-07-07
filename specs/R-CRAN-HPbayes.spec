%global packname  HPbayes
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          3%{?dist}
Summary:          Heligman Pollard mortality model parameter estimation usingBayesian Melding with Incremental Mixture Importance Sampling

License:          Unlimited
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-stats 
BuildRequires:    R-boot 
Requires:         R-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-numDeriv 
Requires:         R-stats 
Requires:         R-boot 

%description
This package provides all the functions necessary to estimate the 8
parameters of the Heligman Pollard mortality model using a Bayesian
Melding procedure with IMIS as well as to convert those parameters into
age-specifc probabilities of death and a corresponding life table

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
