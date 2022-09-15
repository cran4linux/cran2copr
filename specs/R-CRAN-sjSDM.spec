%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sjSDM
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Scalable Joint Species Distribution Modeling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-Ternary 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-mathjaxr 
BuildRequires:    R-CRAN-ggtern 
Requires:         R-CRAN-reticulate 
Requires:         R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-utils 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-abind 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-Metrics 
Requires:         R-parallel 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-Ternary 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-mathjaxr 
Requires:         R-CRAN-ggtern 

%description
A scalable method to estimate joint Species Distribution Models (jSDMs)
for big community datasets based on a Monte Carlo approximation of the
joint likelihood.  The numerical approximation is based on 'PyTorch' and
'reticulate', and can be run on CPUs and GPUs alike. The method is
described in Pichler & Hartig (2021) <doi:10.1111/2041-210X.13687>. The
package contains various extensions, including support for different
response families, ability to account for spatial autocorrelation, and
deep neural networks instead of the linear predictor in jSDMs.

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
