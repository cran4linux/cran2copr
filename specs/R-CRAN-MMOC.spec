%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MMOC
%global packver   0.1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Omic Spectral Clustering using the Flag Manifold

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.58.1
BuildRequires:    R-CRAN-igraph >= 1.4.1
BuildRequires:    R-CRAN-Spectrum >= 1.1
Requires:         R-CRAN-MASS >= 7.3.58.1
Requires:         R-CRAN-igraph >= 1.4.1
Requires:         R-CRAN-Spectrum >= 1.1

%description
Multi-omic (or any multi-view) spectral clustering methods often assume
the same number of clusters across all datasets. We supply methods for
multi-omic spectral clustering when the number of distinct clusters
differs among the omics profiles (views).

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
