%global __brp_check_rpaths %{nil}
%global packname  jmuOutlier
%global packver   2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2
Release:          3%{?dist}%{?buildtag}
Summary:          Permutation Tests for Nonparametric Statistics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0
Requires:         R-core >= 2.0
BuildArch:        noarch

%description
Performs a permutation test on the difference between two location
parameters, a permutation correlation test, a permutation F-test, the
Siegel-Tukey test, a ratio mean deviance test.  Also performs some
graphing techniques, such as for confidence intervals, vector addition,
and Fourier analysis; and includes functions related to the Laplace
(double exponential) and triangular distributions.  Performs power
calculations for the binomial test.

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
