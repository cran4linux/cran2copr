%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nimbleSCR
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Capture-Recapture (SCR) Methods Using 'nimble'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nimble 
BuildRequires:    R-methods 
Requires:         R-CRAN-nimble 
Requires:         R-methods 

%description
Provides utility functions, distributions, and fitting methods for
Bayesian Spatial Capture-Recapture (SCR) and Open Population Spatial
Capture-Recapture (OPSCR) modelling using the nimble package (de Valpine
et al. 2017 <doi:10.1080/10618600.2016.1172487 >). Development of the
package was motivated primarily by the need for flexible and efficient
analysis of large-scale SCR data (Bischof et al. 2020
<doi:10.1073/pnas.2011383117 >). Computational methods and techniques
implemented in nimbleSCR include those discussed in Turek et al. 2021
<doi:10.1002/ecs2.3385>; among others. For a recent application of
nimbleSCR, see Milleret et al. (2021) <doi:10.1098/rsbl.2021.0128>.

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
