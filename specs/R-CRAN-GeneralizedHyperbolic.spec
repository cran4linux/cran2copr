%global packname  GeneralizedHyperbolic
%global packver   0.8-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.4
Release:          3%{?dist}
Summary:          The Generalized Hyperbolic Distribution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-DistributionUtils 
BuildRequires:    R-MASS 
Requires:         R-CRAN-DistributionUtils 
Requires:         R-MASS 

%description
Functions for the hyperbolic and related distributions. Density,
distribution and quantile functions and random number generation are
provided for the hyperbolic distribution, the generalized hyperbolic
distribution, the generalized inverse Gaussian distribution and the
skew-Laplace distribution. Additional functionality is provided for the
hyperbolic distribution, normal inverse Gaussian distribution and
generalized inverse Gaussian distribution, including fitting of these
distributions to data. Linear models with hyperbolic errors may be fitted
using hyperblmFit.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/hyperbWSqTable.R
%doc %{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/INDEX
