%global __brp_check_rpaths %{nil}
%global packname  mmc
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Multivariate Measurement Error Correction

License:          GNU General Public License (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3
BuildRequires:    R-stats >= 2.5.0
BuildRequires:    R-survival >= 2.38.1
Requires:         R-MASS >= 7.3
Requires:         R-stats >= 2.5.0
Requires:         R-survival >= 2.38.1

%description
Provides routines for multivariate measurement error correction. Includes
procedures for linear, logistic and Cox regression models. Bootstrapped
standard errors and confidence intervals can be obtained for corrected
estimates.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
