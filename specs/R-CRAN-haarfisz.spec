%global __brp_check_rpaths %{nil}
%global packname  haarfisz
%global packver   4.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.5.3
Release:          1%{?dist}%{?buildtag}
Summary:          Software to Perform Haar Fisz Transforms

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-wavethresh 
Requires:         R-CRAN-wavethresh 

%description
A Haar-Fisz algorithm for Poisson intensity estimation. Will denoise
Poisson distributed sequences where underlying intensity is not constant.
Uses the multiscale variance-stabilization method called the Haar-Fisz
transform. Contains functions to carry out the forward and inverse
Haar-Fisz transform and denoising on near-Gaussian sequences. Can also
carry out cycle-spinning. Main reference: Fryzlewicz, P. and Nason, G.P.
(2004) "A Haar-Fisz algorithm for Poisson intensity estimation." Journal
of Computational and Graphical Statistics, 13, 621-638.
<doi:10.1198/106186004X2697>.

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
