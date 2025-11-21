%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  scpropreg
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simplicially Constrained Regression Models for Proportions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-Rfast2 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-Rfast2 

%description
Simplicially constrained regression models for proportions in both sides.
The constraint is always that the betas are non-negative and sum to 1.
References: Iverson S.J.., Field C., Bowen W.D. and Blanchard W. (2004)
"Quantitative Fatty Acid Signature Analysis: A New Method of Estimating
Predator Diets". Ecological Monographs, 74(2): 211-235.
<doi:10.1890/02-4105>.

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
