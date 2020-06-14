%global packname  lmvar
%global packver   1.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.2
Release:          2%{?dist}
Summary:          Linear Regression with Non-Constant Variances

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-parallel >= 3.3.0
BuildRequires:    R-graphics >= 3.3.0
BuildRequires:    R-grDevices >= 3.3.0
BuildRequires:    R-stats >= 3.2.5
BuildRequires:    R-CRAN-maxLik >= 1.3.4
BuildRequires:    R-Matrix >= 1.2.4
BuildRequires:    R-CRAN-matrixcalc >= 1.0.3
Requires:         R-parallel >= 3.3.0
Requires:         R-graphics >= 3.3.0
Requires:         R-grDevices >= 3.3.0
Requires:         R-stats >= 3.2.5
Requires:         R-CRAN-maxLik >= 1.3.4
Requires:         R-Matrix >= 1.2.4
Requires:         R-CRAN-matrixcalc >= 1.0.3

%description
Runs a linear-like regression with in which both the expected value and
the variance can vary per observation. The expected values mu follows the
standard linear model mu = X_mu * beta_mu. The standard deviation sigma
follows the model log(sigma) = X_sigma * beta_sigma. The package comes
with two vignettes: 'Intro' gives an introduction, 'Math' gives
mathematical details.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
