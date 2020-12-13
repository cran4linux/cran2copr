%global packname  Zelig
%global packver   5.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Everyone's Statistical Software

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.3.0.2
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-AER 
BuildRequires:    R-CRAN-Amelia 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-geepack 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-MatchIt 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-VGAM 
Requires:         R-CRAN-dplyr >= 0.3.0.2
Requires:         R-CRAN-survival 
Requires:         R-CRAN-AER 
Requires:         R-CRAN-Amelia 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-geepack 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-MatchIt 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-MCMCpack 
Requires:         R-methods 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-VGAM 

%description
A framework that brings together an abundance of common statistical models
found across packages into a unified interface, and provides a common
architecture for estimation and interpretation, as well as bridging
functions to absorb increasingly more models into the package. Zelig
allows each individual package, for each statistical model, to be accessed
by a common uniformly structured call and set of arguments. Moreover,
Zelig automates all the surrounding building blocks of a statistical
work-flow--procedures and algorithms that may be essential to one user's
application but which the original package developer did not use in their
own research and might not themselves support. These include
bootstrapping, jackknifing, and re-weighting of data. In particular, Zelig
automatically generates predicted and simulated quantities of interest
(such as relative risk ratios, average treatment effects, first
differences and predicted and expected values) to interpret and visualize
complex models.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
