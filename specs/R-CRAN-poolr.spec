%global packname  poolr
%global packver   0.8-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.2
Release:          3%{?dist}
Summary:          Methods for Pooling P-Values from (Dependent) Tests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Functions for pooling/combining the results (i.e., p-values) from
(dependent) hypothesis tests. Included are Fisher's method, Stouffer's
method, the inverse chi-square method, the Bonferroni method, Tippett's
method, and the binomial test. Each method can be adjusted based on an
estimate of the effective number of tests or using empirically derived
null distribution using pseudo replicates. For Fisher's, Stouffer's, and
the inverse chi-square method, direct generalizations based on
multivariate theory are also available (leading to Brown's method,
Strube's method, and the generalized inverse chi-square method).

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
