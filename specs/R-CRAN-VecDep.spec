%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  VecDep
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Measuring Copula-Based Dependence Between Random Vectors

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gtools >= 3.9.5
BuildRequires:    R-CRAN-hash >= 2.2.6.3
BuildRequires:    R-CRAN-pbapply >= 1.7.2
BuildRequires:    R-CRAN-magic >= 1.6.1
BuildRequires:    R-CRAN-reticulate >= 1.39.0
BuildRequires:    R-CRAN-HAC >= 1.1.1
BuildRequires:    R-CRAN-covglasso >= 1.0.3
BuildRequires:    R-CRAN-sets >= 1.0.25
BuildRequires:    R-CRAN-expm >= 1.0.0
BuildRequires:    R-CRAN-Rmpfr >= 0.9.5
BuildRequires:    R-CRAN-ElliptCopulas >= 0.1.4.1
Requires:         R-CRAN-gtools >= 3.9.5
Requires:         R-CRAN-hash >= 2.2.6.3
Requires:         R-CRAN-pbapply >= 1.7.2
Requires:         R-CRAN-magic >= 1.6.1
Requires:         R-CRAN-reticulate >= 1.39.0
Requires:         R-CRAN-HAC >= 1.1.1
Requires:         R-CRAN-covglasso >= 1.0.3
Requires:         R-CRAN-sets >= 1.0.25
Requires:         R-CRAN-expm >= 1.0.0
Requires:         R-CRAN-Rmpfr >= 0.9.5
Requires:         R-CRAN-ElliptCopulas >= 0.1.4.1

%description
Provides functions for estimation (parametric, semi-parametric and
non-parametric) of copula-based dependence coefficients between a finite
collection of random vectors, including phi-dependence measures and
Bures-Wasserstein dependence measures. An algorithm for agglomerative
hierarchical variable clustering is also implemented. Following the
articles De Keyser & Gijbels (2024) <doi:10.1016/j.jmva.2024.105336>, De
Keyser & Gijbels (2024) <doi:10.1016/j.ijar.2023.109090>, and De Keyser &
Gijbels (2024) <doi:10.48550/arXiv.2404.07141>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
