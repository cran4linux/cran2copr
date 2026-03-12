%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  WBI
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Wasserstein Bipolarization Index

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-transport 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-bcaboot 
Requires:         R-CRAN-transport 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-bcaboot 

%description
Computation of the Wasserstein Bipolarization Index as described in Lee
and Sobel (Forthcoming) <doi:10.48550/arXiv.2408.03331>. Provides both
asymptotic (Sommerfeld, 2017
<https://ediss.uni-goettingen.de/bitstream/handle/11858/00-1735-0000-0023-3FA1-C/DissertationSommerfeldRev.pdf?sequence=1>)
and bootstrap methods (Efron and Narasimhan, 2020
<doi:10.1080/10618600.2020.1714633>) for calculating confidence intervals.

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
