%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xpose4
%global packver   4.7.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.7.3
Release:          1%{?dist}%{?buildtag}
Summary:          Diagnostics for Nonlinear Mixed-Effect Models

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.2.0
Requires:         R-core >= 2.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-gam 
BuildRequires:    R-splines 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-readr 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-methods 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-gam 
Requires:         R-splines 
Requires:         R-grid 
Requires:         R-CRAN-readr 

%description
A model building aid for nonlinear mixed-effects (population) model
analysis using NONMEM, facilitating data set checkout, exploration and
visualization, model diagnostics, candidate covariate identification and
model comparison. The methods are described in Keizer et al. (2013)
<doi:10.1038/psp.2013.24>, and Jonsson et al. (1999)
<doi:10.1016/s0169-2607(98)00067-4>.

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
