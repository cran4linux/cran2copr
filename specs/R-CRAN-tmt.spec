%global __brp_check_rpaths %{nil}
%global packname  tmt
%global packver   0.3.0-20
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0.20
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of the Rasch Model for Multistage Tests

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-parallel 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 

%description
Provides conditional maximum likelihood (CML) item parameter estimation of
sequential as well as cumulative deterministic multistage designs (Zwitser
& Maris, 2015, <doi:10.1007/s11336-013-9369-6>) as well as probabilistic
sequential and cumulative multistage designs (Steinfeld & Robitzsch, 2021,
<doi:10.31234/osf.io/ew27f>). Supports CML item parameter estimation of
conventional linear designs and additional functions for the likelihood
ratio test (Andersen, 1973, <doi:10.1007/BF02291180>) as well as functions
for the simulation of several kinds of multistage designs.

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
