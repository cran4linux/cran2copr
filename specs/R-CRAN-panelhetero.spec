%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  panelhetero
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Panel Data Analysis with Heterogeneous Dynamics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-KernSmooth 
BuildRequires:    R-CRAN-Rearrangement 
BuildRequires:    R-stats 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-KernSmooth 
Requires:         R-CRAN-Rearrangement 
Requires:         R-stats 

%description
Understanding the dynamics of potentially heterogeneous variables is
important in statistical applications. This package provides tools for
estimating the degree of heterogeneity across cross-sectional units in the
panel data analysis. The methods are developed by Okui and Yanagi (2019)
<doi:10.1016/j.jeconom.2019.04.036> and Okui and Yanagi (2020)
<doi:10.1093/ectj/utz019>.

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
