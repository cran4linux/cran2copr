%global packname  match2C
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Match One Sample using Two Criteria

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rcbalance 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-CRAN-mvnfast 
Requires:         R-stats 
Requires:         R-CRAN-rcbalance 
Requires:         R-utils 

%description
Multivariate matching in observational studies typically has two goals: 1.
to construct treated and control groups that have similar distribution of
observed covariates and 2. to produce matched pairs or sets that are
homogeneous in a few priority variables. This packages implements a
network-based method built around a tripartite graph that can
simultaneously achieve both goals. A detailed 'RMarkdown' tutorial can be
found at <https://github.com/bzhangupenn/match2C/tree/master/tutorial>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
