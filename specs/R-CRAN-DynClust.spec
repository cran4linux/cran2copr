%global __brp_check_rpaths %{nil}
%global packname  DynClust
%global packver   3.24
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.24
Release:          1%{?dist}%{?buildtag}
Summary:          Denoising and Clustering for Dynamical Image Sequence (2D or 3D)+t

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-parallel 
Requires:         R-parallel 

%description
A two-stage procedure for the denoising and clustering of stack of noisy
images acquired over time. Clustering only assumes that the data contain
an unknown but small number of dynamic features. The method first denoises
the signals using local spatial and full temporal information. The
clustering step uses the previous output to aggregate voxels based on the
knowledge of their spatial neighborhood. Both steps use a single keytool
based on the statistical comparison of the difference of two signals with
the null signal. No assumption is therefore required on the shape of the
signals. The data are assumed to be normally distributed (or at least
follow a symmetric distribution) with a known constant variance. Working
pixelwise, the method can be time-consuming depending on the size of the
data-array but harnesses the power of multicore cpus.

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
