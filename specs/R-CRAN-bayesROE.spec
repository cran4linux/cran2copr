%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bayesROE
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Regions of Evidence

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.7.2
BuildRequires:    R-CRAN-golem >= 0.3.3
BuildRequires:    R-CRAN-config >= 0.3.1
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-stats 
Requires:         R-CRAN-shiny >= 1.7.2
Requires:         R-CRAN-golem >= 0.3.3
Requires:         R-CRAN-config >= 0.3.1
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-shinyBS 
Requires:         R-stats 

%description
Computation and visualization of Bayesian Regions of Evidence to
systematically evaluate the sensitivity of a superiority or
non-inferiority claim against any prior assumption of its assessors.
Methodological details are elaborated by Hoefler and Miller (2023)
<https://osf.io/jxnsv>. Besides generic functions, the package also
provides an intuitive 'Shiny' application, that can be run in local R
environments.

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
