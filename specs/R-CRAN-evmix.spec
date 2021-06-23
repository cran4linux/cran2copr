%global __brp_check_rpaths %{nil}
%global packname  evmix
%global packver   2.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.12
Release:          3%{?dist}%{?buildtag}
Summary:          Extreme Value Mixture Modelling, Threshold Estimation andBoundary Corrected Kernel Density Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-MASS 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-grDevices 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-MASS 
Requires:         R-splines 
Requires:         R-CRAN-gsl 
Requires:         R-CRAN-SparseM 
Requires:         R-grDevices 

%description
The usual distribution functions, maximum likelihood inference and model
diagnostics for univariate stationary extreme value mixture models are
provided. Kernel density estimation including various boundary corrected
kernel density estimation methods and a wide choice of kernels, with
cross-validation likelihood based bandwidth estimator. Reasonable
consistency with the base functions in the 'evd' package is provided, so
that users can safely interchange most code.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
