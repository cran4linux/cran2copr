%global packname  cna
%global packver   2.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.3
Release:          3%{?dist}
Summary:          Causal Modeling with Coincidence Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-matrixStats 
Requires:         R-CRAN-Rcpp 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-matrixStats 

%description
Provides comprehensive functionalities for causal modeling with
Coincidence Analysis (CNA), which is a configurational comparative method
of causal data analysis that was first introduced in Baumgartner (2009)
<doi:10.1177/0049124109339369>, and generalized in Baumgartner & Ambuehl
(2018) <doi:10.1017/psrm.2018.45>. CNA is related to Qualitative
Comparative Analysis (QCA), but contrary to the latter, it is custom-built
for uncovering causal structures with multiple outcomes and it builds
causal models from the bottom up by gradually combining single factors to
complex dependency structures until the requested thresholds of model fit
are met. The new functionalities provided by this package version include
functions for evaluating and benchmarking the correctness of CNA's output,
a function determining whether a solution is an INUS model, a function
bringing non-INUS expressions into INUS form, and a function for
identifying cyclic models. The package vignette has been updated
accordingly.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
