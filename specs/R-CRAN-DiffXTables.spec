%global packname  DiffXTables
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}
Summary:          Pattern Heterogeneity via Distributional Differences AcrossContingency Tables

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-Matrix 
Requires:         R-Matrix 

%description
Statistical hypothesis testing of pattern heterogeneity via differences in
underlying distributions across two or more contingency tables. Three
tests are included: the comparative chi-squared test (Song et al, 2014)
<doi:10.1093/nar/gku086> (Zhang et al, 2015) <doi:10.1093/nar/gkv358>, the
Sharma-Song test, and the heterogeneity test. Under the null hypothesis
that row and column variables are statistically independent and joint
distributions are equal, their test statistics all follow an
asymptotically chi-squared distribution. These options test for
heterogeneous patterns that differ in either the first order (marginal) or
the second order (joint distribution deviation from product of marginals).
Second-order differences may reveal more fundamental changes than
first-order differences across heterogeneous patterns.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
