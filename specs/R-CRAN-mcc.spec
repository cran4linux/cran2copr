%global packname  mcc
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Moment Corrected Correlation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
A number of biomedical problems involve performing many hypothesis tests,
with an attendant need to apply stringent thresholds. Often the data take
the form of a series of predictor vectors, each of which must be compared
with a single response vector, perhaps with nuisance covariates.
Parametric tests of association are often used, but can result in
inaccurate type I error at the extreme thresholds, even for large sample
sizes. Furthermore, standard two-sided testing can reduce power compared
to the doubled p-value, due to asymmetry in the null distribution. Exact
(permutation) testing approaches are attractive, but can be
computationally intensive and cumbersome. MCC is an approximation to exact
association testing of two vectors that is accurate and fast enough for
standard use in high-throughput settings, and can easily provide standard
two-sided or doubled p-values.

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
