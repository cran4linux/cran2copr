%global __brp_check_rpaths %{nil}
%global packname  multiviewtest
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Hypothesis Tests for Association Between Subgroups in Two Data Views

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-randnet 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-randnet 
Requires:         R-CRAN-irlba 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 

%description
Tests for association between subgroups in two multivariate data views,
two network data views, or a multivariate data view and a network data
view. (Reference 1: Gao, L.L., Bien, J., and Witten, D. (2020) "Are
Clusterings of Multiple Data Views Independent?",
<doi:10.1093/biostatistics/kxz001> and Reference 2: Gao, L.L., Witten, D.,
Bien, J. (2021) Testing for Association in Multi-View Network Data,
<doi:10.1111/biom.13464>.)

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
