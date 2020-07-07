%global packname  MixSAL
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Mixtures of Multivariate Shifted Asymmetric Laplace (SAL)Distributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS >= 3.1.3
Requires:         R-MASS >= 3.1.3

%description
The current version of the 'MixSAL' package allows users to generate data
from a multivariate SAL distribution or a mixture of multivariate SAL
distributions, evaluate the probability density function of a multivariate
SAL distribution or a mixture of multivariate SAL distributions, and fit a
mixture of multivariate SAL distributions using the
Expectation-Maximization (EM) algorithm (see Franczak et. al, 2014,
<doi:10.1109/TPAMI.2013.216>, for details).

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
%{rlibdir}/%{packname}/INDEX
