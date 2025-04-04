%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lcmm
%global packver   2.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Extended Mixed Models Using Latent Classes and Latent Processes

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-survival >= 2.37.2
BuildRequires:    R-CRAN-marqLevAlg > 2.0
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-spacefillr 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-survival >= 2.37.2
Requires:         R-CRAN-marqLevAlg > 2.0
Requires:         R-CRAN-nlme 
Requires:         R-parallel 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-spacefillr 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-numDeriv 

%description
Estimation of various extensions of the mixed models including latent
class mixed models, joint latent class mixed models, mixed models for
curvilinear outcomes, mixed models for multivariate longitudinal outcomes
using a maximum likelihood estimation method (Proust-Lima, Philipps,
Liquet (2017) <doi:10.18637/jss.v078.i02>).

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
