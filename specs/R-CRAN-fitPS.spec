%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fitPS
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Fit Probability Models to Forensic Survey Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-VGAM 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-ks 
Requires:         R-methods 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-VGAM 

%description
Fits probability models to P- and S-type count data arising from forensic
surveys of clothing for the background presence of glass, paint, and
related trace material. Built-in models include zeta, zero-inflated zeta,
and logarithmic distributions, with a public extension interface for
additional models. Inference is available by maximum likelihood,
parametric Bayesian methods, the ordinary nonparametric bootstrap, and
Rubin's Bayesian Bootstrap. The clothing-survey setting is described by
Coulson, Buckleton, Gummer, and Triggs (2001)
<doi:10.1016/S1355-0306(01)71847-3>.

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
