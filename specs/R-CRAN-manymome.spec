%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  manymome
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Mediation, Moderation and Moderated-Mediation After Model Fitting

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lmhelprs 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-boot 
Requires:         R-parallel 
Requires:         R-CRAN-pbapply 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-lmhelprs 

%description
Computes indirect effects, conditional effects, and conditional indirect
effects in a structural equation model or path model after model fitting,
with no need to define any user parameters or label any paths in the model
syntax, using the approach presented in Cheung and Cheung (2024)
<doi:10.3758/s13428-023-02224-z>. Can also form bootstrap confidence
intervals by doing bootstrapping only once and reusing the bootstrap
estimates in all subsequent computations. Supports bootstrap confidence
intervals for standardized (partially or completely) indirect effects,
conditional effects, and conditional indirect effects as described in
Cheung (2009) <doi:10.3758/BRM.41.2.425> and Cheung, Cheung, Lau, Hui, and
Vong (2022) <doi:10.1037/hea0001188>. Model fitting can be done by
structural equation modeling using lavaan() or regression using lm().

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
