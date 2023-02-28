%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ScreeNOT
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          'ScreeNOT': MSE-Optimal Singular Value Thresholding in Correlated Noise

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Optimal hard thresholding of singular values. The procedure adaptively
estimates the best singular value threshold under unknown noise
characteristics. The threshold chosen by 'ScreeNOT' is optimal
(asymptotically, in the sense of minimum Frobenius error) under the the
so-called "Spiked model" of a low-rank matrix observed in additive noise.
In contrast to previous works, the noise is not assumed to be i.i.d. or
white; it can have an essentially arbitrary and unknown correlation
structure, across either rows, columns or both. 'ScreeNOT' is proposed to
practitioners as a mathematically solid alternative to Cattell's
ever-popular but vague Scree Plot heuristic from 1966. If you use this
package, please cite our paper: David L. Donoho, Matan Gavish and Elad
Romanov (2023). "ScreeNOT: Exact MSE-optimal singular value thresholding
in correlated noise." Annals of Statistics, 2023 (To appear).
<arXiv:2009.12297>.

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
