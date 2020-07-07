%global packname  flip
%global packver   2.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5.0
Release:          3%{?dist}
Summary:          Multivariate Permutation Tests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-cherry 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-someMTP 
Requires:         R-methods 
Requires:         R-CRAN-cherry 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-someMTP 

%description
It implements many univariate and multivariate permutation (and rotation)
tests. Allowed tests: the t one and two samples, ANOVA, linear models, Chi
Squared test, rank tests (i.e. Wilcoxon, Mann-Whitney, Kruskal-Wallis),
Sign test and Mc Nemar. Test on Linear Models are performed also in
presence of covariates (i.e. nuisance parameters). The permutation and the
rotation methods to get the null distribution of the test statistics are
available. It also implements methods for multiplicity control such as
Westfall & Young minP procedure and Closed Testing (Marcus, 1976) and
k-FWER. Moreover, it allows to test for fixed effects in mixed effects
models.

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
%{rlibdir}/%{packname}/INDEX
