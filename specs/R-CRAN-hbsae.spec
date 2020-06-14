%global packname  hbsae
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Hierarchical Bayesian Small Area Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-arm 
Requires:         R-Matrix 
Requires:         R-CRAN-arm 

%description
Functions to compute small area estimates based on a basic area or
unit-level model. The model is fit using restricted maximum likelihood, or
in a hierarchical Bayesian way. In the latter case numerical integration
is used to average over the posterior density for the between-area
variance.  The output includes the model fit, small area estimates and
corresponding MSEs, as well as some model selection measures. Additional
functions provide means to compute aggregate estimates and MSEs, to
minimally adjust the small area estimates to benchmarks at a higher
aggregation level, and to graphically compare different sets of small area
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
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
