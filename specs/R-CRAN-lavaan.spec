%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lavaan
%global packver   0.6-20
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.20
Release:          1%{?dist}%{?buildtag}
Summary:          Latent Variable Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats4 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-pbivnorm 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-quadprog 
Requires:         R-methods 
Requires:         R-stats4 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-pbivnorm 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-quadprog 

%description
Fit a variety of latent variable models, including confirmatory factor
analysis, structural equation modeling and latent growth curve models.

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
