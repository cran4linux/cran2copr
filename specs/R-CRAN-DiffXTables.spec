%global packname  DiffXTables
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Pattern Analysis Across Contingency Tables

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack >= 0.6.1
BuildRequires:    R-CRAN-pander 
Requires:         R-CRAN-Rdpack >= 0.6.1
Requires:         R-CRAN-pander 

%description
Statistical hypothesis testing of pattern heterogeneity via differences in
underlying distributions across multiple contingency tables. Five tests
are included: the comparative chi-squared test (Song et al. 2014)
<doi:10.1093/nar/gku086> (Zhang et al. 2015) <doi:10.1093/nar/gkv358>, the
Sharma-Song test, the heterogeneity test, the marginal-change test (Sharma
et al. 2020), and the strength test (Sharma et al. 2020). Under the null
hypothesis that row and column variables are statistically independent and
joint distributions are equal, their test statistics all follow an
asymptotically chi-squared distribution. A comprehensive type analysis
categorizes the relation among the contingency tables into type null, 0,
1, and 2 (Sharma et al. 2020). They can identify heterogeneous patterns
that differ in either the first order (marginal) or the second order
(joint distribution deviation from product of marginals). Second-order
differences may reveal more fundamental changes than first-order
differences across heterogeneous patterns.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
