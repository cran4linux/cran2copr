%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xemd
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          eXtended Empirical Mode Decomposition

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-pracma 
Requires:         R-splines 
Requires:         R-stats 
Requires:         R-utils 

%description
Signals are decomposed into oscillatory modes by empirical mode
decomposition and its ensemble, complementary ensemble, complete ensemble,
masked, bivariate and multivariate variants, by variational mode
decomposition and its multivariate and successive variants, and by local
mean decomposition, iterative filtering, time varying filter empirical
mode decomposition and the empirical wavelet transform; the
synchrosqueezed wavelet transform is also provided. Empirical mode
decomposition is due to Huang et al. (1998) <doi:10.1098/rspa.1998.0193>,
its ensemble variant to Wu and Huang (2009)
<doi:10.1142/S1793536909000047> and variational mode decomposition to
Dragomiretskiy and Zosso (2014) <doi:10.1109/TSP.2013.2288675>. The modes
can be described by their instantaneous amplitude and frequency and their
Hilbert spectrum, tested as intrinsic mode functions or against white
noise, selected by energy and compared through orthogonality, mode
splitting, reconstruction quality, ensemble dispersion and similarity
measures. Acceleration, velocity and displacement records stored as a long
table of time, value, quantity and component are decomposed for every
record and quantity in one call, with a warning and a regularization of
the time grid when it is not uniform.

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
