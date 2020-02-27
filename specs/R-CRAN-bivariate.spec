%global packname  bivariate
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}
Summary:          Bivariate Probability Distributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-intoo 
BuildRequires:    R-CRAN-barsurf 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-KernSmooth 
Requires:         R-CRAN-intoo 
Requires:         R-CRAN-barsurf 
Requires:         R-CRAN-mvtnorm 
Requires:         R-KernSmooth 

%description
Convenience functions for constructing, plotting and evaluating bivariate
probability distributions, including their probability mass/density
functions and cumulative distribution functions. Supports uniform
(discrete and continuous), binomial, Poisson, categorical, normal, bimodal
and Dirichlet (trivariate) distributions, and kernel smoothing and
empirical cumulative distribution functions.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
