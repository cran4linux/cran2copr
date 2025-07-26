%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nlive
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Estimation of Sigmoidal and Piecewise Linear Mixed Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-nlraa 
BuildRequires:    R-CRAN-sqldf 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-lcmm 
BuildRequires:    R-CRAN-saemix 
BuildRequires:    R-CRAN-Rmisc 
BuildRequires:    R-CRAN-sitar 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-fastDummies 
BuildRequires:    R-CRAN-Rmpfr 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-nlraa 
Requires:         R-CRAN-sqldf 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-CRAN-lcmm 
Requires:         R-CRAN-saemix 
Requires:         R-CRAN-Rmisc 
Requires:         R-CRAN-sitar 
Requires:         R-stats 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-fastDummies 
Requires:         R-CRAN-Rmpfr 
Requires:         R-splines 
Requires:         R-CRAN-viridis 

%description
Estimation of relatively complex nonlinear mixed-effects models, including
the Sigmoidal Mixed Model and the Piecewise Linear Mixed Model with abrupt
or smooth transition, through a single intuitive line of code and with
automated generation of starting values.

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
