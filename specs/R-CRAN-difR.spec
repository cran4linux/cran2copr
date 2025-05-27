%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  difR
%global packver   6.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Collection of Methods to Detect Dichotomous and Polytomous Differential Item Functioning (DIF)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mirt 
BuildRequires:    R-CRAN-ltm 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-deltaPlotR 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-glmnet 
Requires:         R-CRAN-mirt 
Requires:         R-CRAN-ltm 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-deltaPlotR 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-glmnet 

%description
Methods to detect differential item functioning (DIF) in dichotomous and
polytomous items, using both classical and modern approaches. These
include Mantel-Haenszel procedures, logistic regression (including ordinal
models), and regularization-based methods such as LASSO. Uniform and
non-uniform DIF effects can be detected, and some methods support multiple
focal groups. The package also provides tools for anchor purification,
rest score matching, effect size estimation, and DIF simulation. See
Magis, Beland, Tuerlinckx, and De Boeck (2010, Behavior Research Methods,
42, 847–862, <doi:10.3758/BRM.42.3.847>) for a general overview.

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
