%global packname  borrowr
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate Causal Effects with Borrowing Between Data Sources

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-BART >= 2.1
BuildRequires:    R-CRAN-mvtnorm >= 1.0.8
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-BART >= 2.1
Requires:         R-CRAN-mvtnorm >= 1.0.8
Requires:         R-CRAN-Rcpp >= 1.0.0

%description
Estimate population average treatment effects from a primary data source
with borrowing from supplemental sources. Causal estimation is done with
either a Bayesian linear model or with Bayesian additive regression trees
(BART) to adjust for confounding. Borrowing is done with multisource
exchangeability models (MEMs). For information on BART, see Chipman,
George, & McCulloch (2010) <doi:10.1214/09-AOAS285>. For information on
MEMs, see Kaizer, Koopmeiners, & Hobbs (2018)
<doi:10.1093/biostatistics/kxx031>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
