%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ENMTools
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Niche Evolution using Niche and Distribution Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-raster >= 3.6.3
BuildRequires:    R-CRAN-dismo 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ENMeval 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-spatstat.random 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-terra 
Requires:         R-CRAN-raster >= 3.6.3
Requires:         R-CRAN-dismo 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ENMeval 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat.random 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-terra 

%description
Constructing niche models and analyzing patterns of niche evolution.  Acts
as an interface for many popular modeling algorithms, and allows users to
conduct Monte Carlo tests to address basic questions in evolutionary
ecology and biogeography.  Warren, D.L., R.E. Glor, and M. Turelli (2008)
<doi:10.1111/j.1558-5646.2008.00482.x> Glor, R.E., and D.L. Warren (2011)
<doi:10.1111/j.1558-5646.2010.01177.x> Warren, D.L., R.E. Glor, and M.
Turelli (2010) <doi:10.1111/j.1600-0587.2009.06142.x> Cardillo, M., and
D.L. Warren (2016) <doi:10.1111/geb.12455> D.L. Warren, L.J. Beaumont, R.
Dinnage, and J.B. Baumgartner (2019) <doi:10.1111/ecog.03900>.

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
