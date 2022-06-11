%global __brp_check_rpaths %{nil}
%global packname  zetadiv
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Functions to Compute Compositional Turnover Using Zeta Diversity

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-scam 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-geodist 
BuildRequires:    R-CRAN-nnls 
BuildRequires:    R-CRAN-glm2 
Requires:         R-CRAN-scam 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-car 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-geodist 
Requires:         R-CRAN-nnls 
Requires:         R-CRAN-glm2 

%description
Functions to compute compositional turnover using zeta-diversity, the
number of species shared by multiple assemblages. The package includes
functions to compute zeta-diversity for a specific number of assemblages
and to compute zeta-diversity for a range of numbers of assemblages. It
also includes functions to explain how zeta-diversity varies with distance
and with differences in environmental variables between assemblages, using
generalised linear models, linear models with negative constraints,
generalised additive models,shape constrained additive models, and
I-splines.

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
