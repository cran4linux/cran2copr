%global __brp_check_rpaths %{nil}
%global packname  rPACI
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Placido Analysis of Corneal Irregularity

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-bnlearn 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-bnlearn 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-rlang 

%description
Analysis of corneal data obtained from a Placido disk corneal topographer
with calculation of irregularity indices. This package performs analyses
of corneal data obtained from a Placido disk corneal topographer, with the
calculation of the Placido irregularity indices and the posterior
analysis. The package is intended to be easy to use by a practitioner,
providing a simple interface and yielding easily interpretable results. A
corneal topographer is an ophthalmic clinical device that obtains
measurements in the cornea (the anterior part of the eye). A Placido disk
corneal topographer makes use of the Placido disk [Rowsey et al.
(1981)]<doi:10.1001/archopht.1981.03930011093022>, which produce a
circular pattern of measurement nodes. The raw information measured by
such a topographer is used by practitioners to analyze curvatures, to
study optical aberrations, or to diagnose specific conditions of the eye
(e.g. keratoconus, an important corneal disease). The rPACI package allows
the calculation of the corneal irregularity indices described in
[Castro-Luna et al. (2020)]<doi:10.1016%%2Fj.clae.2019.12.006>,
[Ramos-Lopez et al. (2013)]<doi:10.1097%%2FOPX.0b013e3182843f2a>, and
[Ramos-Lopez et al. (2011)]<doi:10.1097/opx.0b013e3182279ff8>. It provides
a simple interface to read corneal topography data files as exported by a
typical Placido disk topographer, to compute the irregularity indices
mentioned before, and to display summary plots that are easy to interpret
for a clinician.

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
