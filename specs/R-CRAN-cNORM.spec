%global packname  cNORM
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Continuous Norming

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-leaps >= 3.0
BuildRequires:    R-CRAN-latticeExtra >= 0.6
BuildRequires:    R-lattice >= 0.20
Requires:         R-CRAN-leaps >= 3.0
Requires:         R-CRAN-latticeExtra >= 0.6
Requires:         R-lattice >= 0.20

%description
Conventional methods for producing standard scores in psychometrics or
biometrics are often plagued with "jumps" or "gaps" (i.e.,
discontinuities) in norm tables and low confidence for assessing extreme
scores. The continuous norming method introduced by A. Lenhard et al.
(2016), <doi:10.1177/1073191116656437>, generates continuous test norm
scores on the basis of the raw data from standardization samples, without
requiring assumptions about the distribution of the raw data: Norm scores
are directly established from raw data by modeling the latter ones as a
function of both percentile scores and an explanatory variable (e.g.,
age). The method minimizes bias arising from sampling and measurement
error, while handling marked deviations from normality, addressing bottom
or ceiling effects and capturing almost all of the variance in the
original norm data sample.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
