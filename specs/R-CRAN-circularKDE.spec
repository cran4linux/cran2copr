%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  circularKDE
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Recent Methods for Kernel Density Estimation of Circular Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-circular 
Requires:         R-CRAN-cli 

%description
Provides recent kernel density estimation methods for circular data,
including adaptive and higher-order techniques. The implementation is
based on recent advances in bandwidth selection and circular smoothing.
Key methods include adaptive bandwidth selection methods by Zámečník et
al. (2024) <doi:10.1007/s00180-023-01401-0>, complete cross-validation by
Hasilová et al. (2024) <doi:10.59170/stattrans-2024-024>, Fourier-based
plug-in rules by Tenreiro (2022) <doi:10.1080/10485252.2022.2057974>, and
higher-order kernels by Tsuruta & Sagae (2017)
<doi:10.1016/j.spl.2017.08.003>.

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
