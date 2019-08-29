%global packname  cbsem
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Simulation, Estimation and Segmentation of Composite BasedStructural Equation Models

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
The composites are linear combinations of their indicators in composite
based structural equation models. Structural models are considered
consisting of two blocks. The indicators of the exogenous composites are
named by X, the indicators of the endogenous by Y. Reflective relations
are given by arrows pointing from the composite to their indicators. Their
values are called loadings.  In a reflective-reflective scenario all
indicators have loadings. Arrows are pointing to their indicators only
from the endogenous composites in the formative-reflective scenario. There
are no loadings at all in the formative-formative scenario. The covariance
matrices are computed for these three scenarios. They can be used to
simulate these models. These models can also be estimated and a
segmentation procedure is included as well.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
