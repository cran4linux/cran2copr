%global packname  npcp
%global packver   0.1-11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.11
Release:          1%{?dist}
Summary:          Some Nonparametric CUSUM Tests for Change-Point Detection inPossibly Multivariate Observations

License:          GPL (>= 3) | file LICENCE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Provides nonparametric CUSUM tests for detecting changes in possibly
serially dependent univariate or multivariate observations. Tests
sensitive to changes in the expectation, the variance, the covariance, the
autocovariance, the distribution function, Spearman's rho, Kendall's tau,
Gini's mean difference, and the copula are provided, as well as a test for
detecting changes in the distribution of independent block maxima (with
environmental studies in mind). The latest additions are a test sensitive
to changes in the autocopula and a combined test of stationarity sensitive
to changes in the distribution function and the autocopula.

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
%license %{rlibdir}/%{packname}/LICENCE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
