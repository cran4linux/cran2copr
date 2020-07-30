%global packname  ENMTools
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Analysis of Niche Evolution using Niche and Distribution Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-dismo 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ENMeval 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-rgdal 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-dismo 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ENMeval 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-rgdal 

%description
Description: Tools for constructing niche models and analyzing patterns of
niche evolution.  Acts as an interface for many popular modeling
algorithms, and allows users to conduct Monte Carlo tests to address basic
questions in evolutionary ecology and biogeography.  Warren, D.L., R.E.
Glor, and M. Turelli (2008) <doi:10.1111/j.1558-5646.2008.00482.x> Glor,
R.E., and D.L. Warren (2011) <doi:10.1111/j.1558-5646.2010.01177.x>
Warren, D.L., R.E. Glor, and M. Turelli (2010)
<doi:10.1111/j.1600-0587.2009.06142.x> Cardillo, M., and D.L. Warren
(2016) <doi:10.1111/geb.12455> D.L. Warren, L.J. Beaumont, R. Dinnage, and
J.B. Baumgartner (2019) <doi:10.1111/ecog.03900>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
