%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SurvSparse
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Survival Analysis with Sparse Longitudinal Covariates

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-gaussquad 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
Requires:         R-splines 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-gaussquad 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 

%description
Survival analysis with sparse longitudinal covariates under right
censoring scheme. Different hazards models are involved. Please cite the
manuscripts corresponding to this package: Sun, Z. et al. (2022)
<doi:10.1007/s10985-022-09548-6>, Sun, Z. and Cao, H. (2023)
<arXiv:2310.15877> and Sun, D. et al. (2023) <arXiv:2308.15549>.

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
