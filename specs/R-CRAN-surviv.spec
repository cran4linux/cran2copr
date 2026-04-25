%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  surviv
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Flexible Instrumental Variable Methods for Survival Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-survival >= 3.4.0
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-rootSolve 
Requires:         R-CRAN-survival >= 3.4.0
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-rootSolve 

%description
Instrumental variable analysis methods for causal inference on survival
data based on the Cox model allowing for various treatment and effect
types, including orthogonality method-of-moments instrumental variable
estimation for the Cox model, two-stage residual inclusion Cox estimation
with frailty, sequential trial emulation, sequential Cox analyses, and
sequential two-stage residual inclusion Cox analyses. Methodological
background includes MacKenzie et al. (2014)
<doi:10.1007/s10742-014-0117-x>, Martinez-Camblor et al. (2019)
<doi:10.1093/biostatistics/kxx062>, Martinez-Camblor et al. (2019)
<doi:10.1111/rssc.12341>, Gran et al. (2010) <doi:10.1002/sim.4048>, and
Keogh et al. (2023) <doi:10.1002/sim.9718>.

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
