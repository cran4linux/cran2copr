%global __brp_check_rpaths %{nil}
%global packname  lcmm
%global packver   1.9.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.3
Release:          1%{?dist}%{?buildtag}
Summary:          Extended Mixed Models Using Latent Classes and Latent Processes

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-CRAN-survival >= 2.37.2
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-survival >= 2.37.2
Requires:         R-parallel 
Requires:         R-CRAN-mvtnorm 

%description
Estimation of various extensions of the mixed models including latent
class mixed models, joint latent latent class mixed models and mixed
models for curvilinear univariate or multivariate longitudinal outcomes
using a maximum likelihood estimation method (Proust-Lima, Philipps,
Liquet (2017) <doi:10.18637/jss.v078.i02>).

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
