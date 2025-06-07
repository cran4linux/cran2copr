%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CBASSED50
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Process CBASS-Derived PAM Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-drc 
BuildRequires:    R-CRAN-rlog 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-drc 
Requires:         R-CRAN-rlog 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-glue 

%description
Tools to process CBASS-derived PAM data efficiently. Minimal requirements
are PAM-based photosynthetic efficiency data (or data from any other
continuous variable that changes with temperature, e.g. relative bleaching
scores) from 4 coral samples (nubbins) subjected to 4 temperature profiles
of at least 2 colonies from 1 coral species from 1 site. Please refer to
the following CBASS (Coral Bleaching Automated Stress System) papers for
in-depth information regarding CBASS acute thermal stress assays,
experimental design considerations, and ED5/ED50/ED95 thermal parameters:
Nicolas R. Evensen et al. (2023) <doi:10.1002/lom3.10555> Christian R.
Voolstra et al. (2020) <doi:10.1111/gcb.15148> Christian R. Voolstra et
al. (2025) <doi:10.1146/annurev-marine-032223-024511>.

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
