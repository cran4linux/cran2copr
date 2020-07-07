%global packname  LDOD
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Finding Locally D-optimal optimal designs for some nonlinear andgeneralized linear models.

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-Rmpfr 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-Rmpfr 

%description
this package provides functions for Finding Locally D-optimal designs for
Logistic, Negative Binomial, Poisson, Michaelis-Menten, Exponential,
Log-Linear, Emax, Richards, Weibull and Inverse Quadratic regression
models and also functions for auto-constructing Fisher information matrix
and Frechet derivative based on some input variables and without
user-interfere.

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
