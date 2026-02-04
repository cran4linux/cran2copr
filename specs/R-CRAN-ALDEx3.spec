%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ALDEx3
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Linear Models for Sequence Count Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-lmerTest 
Requires:         R-parallel 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-matrixStats 
Requires:         R-methods 
Requires:         R-stats 

%description
Provides scalable generalized linear and mixed effects models tailored for
sequence count data analysis (e.g., analysis of 16S or RNA-seq data). Uses
Dirichlet-multinomial sampling to quantify uncertainty in relative
abundance or relative expression conditioned on observed count data.
Implements scale models as a generalization of normalizations which
account for uncertainty in scale (e.g., total abundances) as described in
Nixon et al. (2025) <doi:10.1186/s13059-025-03609-3> and McGovern et al.
(2025) <doi:10.1101/2025.08.05.668734>.

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
