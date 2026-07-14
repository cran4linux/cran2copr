%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  parasiteR
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Theorical-Practical Approach to Parasitological Data Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-BlakerCI 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-binom 
BuildRequires:    R-CRAN-bbmle 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-stats 
Requires:         R-CRAN-BlakerCI 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-binom 
Requires:         R-CRAN-bbmle 
Requires:         R-CRAN-MASS 

%description
Standardizes and streamlines the processing of parasitological data by
integrating descriptive analyses of parasite count distributions,
automated calculation of parasitological indices and their dispersion
measures, and intuitive visualizations for representing these metrics
(Bush et al. 1997 <doi:10.2307/3284227>, Reiczigel et al. 2019
<doi:10.1016/j.pt.2019.01.003>).

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
