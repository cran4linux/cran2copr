%global packname  Kernelheaping
%global packver   2.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.2
Release:          3%{?dist}
Summary:          Kernel Density Estimation for Heaped and Rounded Data

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-sparr 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-fastmatch 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-MASS 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-sparr 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-fastmatch 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-mvtnorm 

%description
In self-reported or anonymised data the user often encounters heaped data,
i.e. data which are rounded (to a possibly different degree of
coarseness). While this is mostly a minor problem in parametric density
estimation the bias can be very large for non-parametric methods such as
kernel density estimation. This package implements a partly Bayesian
algorithm treating the true unknown values as additional parameters and
estimates the rounding parameters to give a corrected kernel density
estimate. It supports various standard bandwidth selection methods.
Varying rounding probabilities (depending on the true value) and
asymmetric rounding is estimable as well: Gross, M. and Rendtel, U. (2016)
(<doi:10.1093/jssam/smw011>). Additionally, bivariate non-parametric
density estimation for rounded data, Gross, M. et al. (2016)
(<doi:10.1111/rssa.12179>), as well as data aggregated on areas is
supported.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
