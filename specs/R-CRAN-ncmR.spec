%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ncmR
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fit Neutral Community Model to Microbiome or Ecological Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 4.0.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-showtext 
Requires:         R-CRAN-ggplot2 >= 4.0.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggtext 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-showtext 

%description
Provides tools for fitting the neutral community model (NCM) to assess the
role of stochastic processes in community assembly. The package implements
the framework of Sloan et al. (2006)
<doi:10.1111/j.1462-2920.2005.00956.x>, enabling users to evaluate neutral
dynamics in ecological and microbial communities.

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
