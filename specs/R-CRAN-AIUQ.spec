%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AIUQ
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Ab Initio Uncertainty Quantification

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-SuperGauss >= 2.0.3
BuildRequires:    R-CRAN-plot3D >= 1.4
BuildRequires:    R-CRAN-fftwtools >= 0.9.11
BuildRequires:    R-methods 
Requires:         R-CRAN-SuperGauss >= 2.0.3
Requires:         R-CRAN-plot3D >= 1.4
Requires:         R-CRAN-fftwtools >= 0.9.11
Requires:         R-methods 

%description
Uncertainty quantification and inverse estimation by probabilistic
generative models from the beginning of the data analysis. An example is a
Fourier basis method for inverse estimation in scattering analysis of
microscopy videos. It does not require specifying a certain range of
Fourier bases and it substantially reduces computational cost via the
generalized Schur algorithm. See the reference: Mengyang Gu, Yue He, Xubo
Liu and Yimin Luo (2023), <arXiv:2309.02468>.

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
