%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OneStep
%global packver   0.9.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.3
Release:          1%{?dist}%{?buildtag}
Summary:          One-Step Estimation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-extraDistr 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-numDeriv 
Requires:         R-parallel 
Requires:         R-CRAN-extraDistr 

%description
Provide principally an eponymic function that numerically computes the Le
Cam's one-step estimator for an independent and identically distributed
sample. One-step estimation is asymptotically efficient (see L. Le Cam
(1956) <https://projecteuclid.org/euclid.bsmsp/1200501652>) and can be
computed faster than the maximum likelihood estimator for large
observation samples, see e.g. Brouste et al. (2021)
<doi:10.32614/RJ-2021-044>.

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
