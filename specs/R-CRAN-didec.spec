%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  didec
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Directed Dependence Coefficient

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-graphics >= 4.3.0
BuildRequires:    R-stats >= 4.3.0
BuildRequires:    R-CRAN-gtools >= 3.9.5
BuildRequires:    R-CRAN-ggplot2 >= 3.4.4
BuildRequires:    R-CRAN-RANN >= 2.6.1
BuildRequires:    R-CRAN-copBasic >= 2.2.3
BuildRequires:    R-CRAN-phylogram >= 2.1.0
BuildRequires:    R-CRAN-pcaPP >= 2.0.5
BuildRequires:    R-CRAN-dendextend >= 1.17.1
BuildRequires:    R-CRAN-rlang >= 1.1.4
BuildRequires:    R-CRAN-cowplot >= 1.1.2
BuildRequires:    R-grDevices >= 0.5.1
BuildRequires:    R-CRAN-FOCI >= 0.1.3
Requires:         R-graphics >= 4.3.0
Requires:         R-stats >= 4.3.0
Requires:         R-CRAN-gtools >= 3.9.5
Requires:         R-CRAN-ggplot2 >= 3.4.4
Requires:         R-CRAN-RANN >= 2.6.1
Requires:         R-CRAN-copBasic >= 2.2.3
Requires:         R-CRAN-phylogram >= 2.1.0
Requires:         R-CRAN-pcaPP >= 2.0.5
Requires:         R-CRAN-dendextend >= 1.17.1
Requires:         R-CRAN-rlang >= 1.1.4
Requires:         R-CRAN-cowplot >= 1.1.2
Requires:         R-grDevices >= 0.5.1
Requires:         R-CRAN-FOCI >= 0.1.3

%description
Directed Dependence Coefficient (didec) is a measure of functional
dependence. Multivariate Feature Ordering by Conditional Independence
(MFOCI) is a variable selection algorithm based on didec. Hierarchical
Variable Clustering (VarClustPartition) is a variable clustering method
based on didec. For more information, see the paper by Ansari and Fuchs
(2025, <doi:10.48550/arXiv.2212.01621>), and the paper by Fuchs and Wang
(2024, <doi:10.1016/j.ijar.2024.109185>).

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
