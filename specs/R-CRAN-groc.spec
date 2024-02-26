%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  groc
%global packver   1.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.9
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Regression on Orthogonal Components

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-rrcov 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-MASS 

%description
Robust multiple or multivariate linear regression, nonparametric
regression on orthogonal components, classical or robust partial least
squares models as described in Bilodeau, Lafaye De Micheaux and Mahdi
(2015) <doi:10.18637/jss.v065.i01>.

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
