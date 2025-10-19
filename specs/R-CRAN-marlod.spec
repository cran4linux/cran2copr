%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  marlod
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Marginal Modeling for Exposure Data with Values Below the LOD

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-utils 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-quantreg 
Requires:         R-stats 
Requires:         R-CRAN-knitr 
Requires:         R-utils 

%description
Functions of marginal mean and quantile regression models are used to
analyze environmental exposure and biomonitoring data with repeated
measurements and non-detects (i.e., values below the limit of detection
(LOD)), as well as longitudinal exposure data that include non-detects and
time-dependent covariates. For more details see Chen IC, Bertke SJ, Curwin
BD (2021) <doi:10.1038/s41370-021-00345-1>, Chen IC, Bertke SJ, Estill CF
(2024) <doi:10.1038/s41370-024-00640-7>, Chen IC, Bertke SJ, Dahm MM
(2024) <doi:10.1093/annweh/wxae068>, and Chen IC (2025)
<doi:10.1038/s41370-025-00752-8>.

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
