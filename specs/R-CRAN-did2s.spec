%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  did2s
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Two-Stage Difference-in-Differences Following Gardner (2021)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fixest >= 0.13.2
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-did 
BuildRequires:    R-CRAN-didimputation 
BuildRequires:    R-CRAN-dreamerr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-HonestDiD 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-staggered 
BuildRequires:    R-stats 
Requires:         R-CRAN-fixest >= 0.13.2
Requires:         R-CRAN-boot 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-did 
Requires:         R-CRAN-didimputation 
Requires:         R-CRAN-dreamerr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-HonestDiD 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-staggered 
Requires:         R-stats 

%description
Estimates Two-way Fixed Effects difference-in-differences/event-study
models using the approach proposed by Gardner (2021)
<doi:10.48550/arXiv.2207.05943>. To avoid the problems caused by OLS
estimation of the Two-way Fixed Effects model, this function first
estimates the fixed effects and covariates using untreated observations
and then in a second stage, estimates the treatment effects.

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
