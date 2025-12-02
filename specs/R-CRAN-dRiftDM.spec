%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dRiftDM
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating (Time-Dependent) Drift Diffusion Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-mirai 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-DEoptim 
BuildRequires:    R-CRAN-dfoptim 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-coda 
Requires:         R-CRAN-withr 
Requires:         R-parallel 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-mirai 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-DEoptim 
Requires:         R-CRAN-dfoptim 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-progress 
Requires:         R-stats 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-coda 

%description
Fit and explore Drift Diffusion Models (DDMs), a common tool in psychology
for describing decision processes in simple tasks. It can handle both
time-independent and time-dependent DDMs. You either choose prebuilt
models or create your own, and the package takes care of model predictions
and parameter estimation. Model predictions are derived via the numerical
solutions provided by Richter, Ulrich, and Janczyk (2023,
<doi:10.1016/j.jmp.2023.102756>).

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
