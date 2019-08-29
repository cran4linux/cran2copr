%global packname  ConfIntVariance
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Confidence Interval for the Univariate Population Variancewithout Normality Assumption

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Surrounds the usual sample variance of a univariate numeric sample with a
confidence interval for the population variance. This has been done so far
only under the assumption that the underlying distribution is normal.
Under the hood, this package implements the unique least-variance unbiased
estimator of the variance of the sample variance, in a formula that is
equivalent to estimating kurtosis and square of the population variance in
an unbiased way and combining them according to the classical formula into
an estimator of the variance of the sample variance. Both the sample
variance and the estimator of its variance are U-statistics. By the theory
of U-statistic, the resulting estimator is unique. See Fuchs,
Krautenbacher (2016) <doi:10.1080/15598608.2016.1158675> and the
references therein for an overview of unbiased estimation of variances of
U-statistics.

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
%{rlibdir}/%{packname}/INDEX
