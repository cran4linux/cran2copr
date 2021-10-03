%global __brp_check_rpaths %{nil}
%global packname  amanpg
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Alternating Manifold Proximal Gradient Method for Sparse PCA

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
Alternating Manifold Proximal Gradient Method for Sparse PCA uses the
Alternating Manifold Proximal Gradient (AManPG) method to find sparse
principal components from a data or covariance matrix. Provides a novel
algorithm for solving the sparse principal component analysis problem
which provides advantages over existing methods in terms of efficiency and
convergence guarantees. Chen, S., Ma, S., Xue, L., & Zou, H. (2020)
<doi:10.1287/ijoo.2019.0032>. Zou, H., Hastie, T., & Tibshirani, R. (2006)
<doi:10.1198/106186006X113430>. Zou, H., & Xue, L. (2018)
<doi:10.1109/JPROC.2018.2846588>.

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
