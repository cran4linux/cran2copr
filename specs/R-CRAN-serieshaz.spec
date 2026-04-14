%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  serieshaz
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Series System Distributions from Dynamic Failure Rate Components

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-flexhaz 
BuildRequires:    R-CRAN-algebraic.dist 
BuildRequires:    R-CRAN-likelihood.model 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-flexhaz 
Requires:         R-CRAN-algebraic.dist 
Requires:         R-CRAN-likelihood.model 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-numDeriv 

%description
Compose multiple dynamic failure rate distributions into series system
distributions where the system hazard equals the sum of component hazards.
Supports hazard, survival, cumulative distribution function, density,
sampling, and maximum likelihood estimation fitting via the dfr_dist()
class from 'flexhaz'. Methods for series system reliability follow Barlow
and Proschan (1975, ISBN:0898713692).

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
