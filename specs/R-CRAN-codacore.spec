%global __brp_check_rpaths %{nil}
%global packname  codacore
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Learning Sparse Log-Ratios for Compositional Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gtools >= 3.8
BuildRequires:    R-CRAN-R6 >= 2.5
BuildRequires:    R-CRAN-keras >= 2.3
BuildRequires:    R-CRAN-tensorflow >= 2.1
BuildRequires:    R-CRAN-pROC >= 1.17
Requires:         R-CRAN-gtools >= 3.8
Requires:         R-CRAN-R6 >= 2.5
Requires:         R-CRAN-keras >= 2.3
Requires:         R-CRAN-tensorflow >= 2.1
Requires:         R-CRAN-pROC >= 1.17

%description
In the context of high-throughput genetic data, CoDaCoRe identifies a set
of sparse biomarkers that are predictive of a response variable of
interest (Gordon-Rodriguez et al., 2021)
<doi:10.1093/bioinformatics/btab645>. More generally, CoDaCoRe can be
applied to any regression problem where the independent variable is
Compositional (CoDa), to derive a set of scale-invariant log-ratios (ILR
or SLR) that are maximally associated to a dependent variable.

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
