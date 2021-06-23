%global __brp_check_rpaths %{nil}
%global packname  peperr
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Parallelised Estimation of Prediction Error

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-snowfall 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-snowfall 
Requires:         R-CRAN-survival 

%description
Designed for prediction error estimation through resampling techniques,
possibly accelerated by parallel execution on a compute cluster. Newly
developed model fitting routines can be easily incorporated. Methods used
in the package are detailed in Porzelius Ch., Binder H. and Schumacher M.
(2009) <doi:10.1093/bioinformatics/btp062> and were used, for instance, in
Porzelius Ch., Schumacher M.and Binder H. (2011)
<doi:10.1007/s00180-011-0236-6>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
