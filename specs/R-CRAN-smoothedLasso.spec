%global packname  smoothedLasso
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          Smoothed LASSO Regression via Nesterov Smoothing

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-Rdpack 
Requires:         R-Matrix 

%description
We provide full functionality to compute smoothed LASSO regression
estimates. For this, the LASSO objective function is first smoothed using
Nesterov smoothing (see Y. Nesterov (2005)
<doi:10.1007/s10107-004-0552-5>), resulting in a modified LASSO objective
function with explicit gradients everywhere. The smoothed objective
function and its gradient are used to minimize it via BFGS, and the
obtained minimizer is returned. Using Nesterov smoothing, the smoothed
LASSO objective function can be made arbitrarily close to the original
(unsmoothed) one. In particular, the Nesterov approach has the advantage
that it comes with explicit accuracy bounds, both on the L1/L2 difference
of the unsmoothed to the smoothed LASSO objective function as well as on
their respective minimizers. A progressive smoothing approach is provided
which iteratively smoothes the LASSO, resulting in more stable regression
estimates.

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
%{rlibdir}/%{packname}/INDEX
