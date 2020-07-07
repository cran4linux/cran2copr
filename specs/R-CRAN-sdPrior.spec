%global packname  sdPrior
%global packver   1.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Scale-Dependent Hyperpriors in Structured AdditiveDistributional Regression

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-GB2 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pscl 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-mgcv 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
Requires:         R-splines 
Requires:         R-CRAN-GB2 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-CRAN-pscl 
Requires:         R-CRAN-mvtnorm 
Requires:         R-mgcv 
Requires:         R-graphics 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 

%description
Utility functions for scale-dependent and alternative hyperpriors. The
distribution parameters may capture location, scale, shape, etc. and every
parameter may depend on complex additive terms (fixed, random, smooth,
spatial, etc.) similar to a generalized additive model. Hyperpriors for
all effects can be elicitated within the package. Including complex tensor
product interaction terms and variable selection priors. The basic model
is explained in in Klein and Kneib (2016) <doi:10.1214/15-BA983>.

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
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
