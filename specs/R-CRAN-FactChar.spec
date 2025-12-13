%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FactChar
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Characterization and Diagnostic Tools for Factorial Block Designs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 

%description
Description: Provides comprehensive tools for analysing and characterizing
mixed-level factorial designs arranged in blocks. Includes construction
and validation of incidence structures, computation of C-matrices,
evaluation of A-, D-, E-, and MV-efficiencies, checking of orthogonal
factorial structure (OFS), diagnostics based on Hamming distance,
discrepancy measures, B-criterion, Es^2 statistics, J2-distance and
J2-efficiency, Phi-p optimality, and symmetry conditions for universal
optimality. The methodological framework follows foundational work on
factorial and mixed-level design assessment by Xu and Wu (2001)
<doi:10.1214/aos/1013699993>, and Gupta (1983)
<doi:10.1111/j.2517-6161.1983.tb01253.x>. These methods assist in
selecting, comparing, and studying factorial block designs across a range
of experimental situations.

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
