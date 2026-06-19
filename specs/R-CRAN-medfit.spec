%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  medfit
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Infrastructure for Mediation Model Fitting and Extraction

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-S7 >= 0.1.0
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-S7 >= 0.1.0
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-MASS 

%description
Provides S7-based infrastructure for fitting mediation models, extracting
path coefficients, and performing bootstrap inference. Designed as a
foundation package for the mediation analysis ecosystem, supporting
'probmed', 'RMediation', and 'medrobust' packages. Implements unified
interfaces for model fitting across different engines (currently
generalized linear models, with future support for mixed models and
Bayesian methods), standardized extraction of mediation paths from various
model types, and robust bootstrap inference methods. Mediation inference
methods are described in MacKinnon, Lockwood and Williams (2004)
<doi:10.1207/s15327906mbr3901_4> and Tofighi and MacKinnon (2011)
<doi:10.3758/s13428-011-0076-x>.

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
