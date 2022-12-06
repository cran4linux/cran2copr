%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sitepickR
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Two-Level Sample Selection with Optimal Site Replacement

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-MatchIt 
BuildRequires:    R-CRAN-sampling 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-MatchIt 
Requires:         R-CRAN-sampling 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-data.table 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-scales 

%description
Carries out a two-level sample selection where the possibility of an
initially selected site not wanting to participate is anticipated, and the
site is optimally replaced. The procedure aims to reduce bias (and/or loss
of external validity) with respect to the target population. In selecting
units and sub-units, 'sitepickR' uses the cube method developed by
'Deville & Tillé', (2004)
<http://www.math.helsinki.fi/msm/banocoss/Deville_Tille_2004.pdf> and
described in Tillé (2011)
<https://www150.statcan.gc.ca/n1/en/pub/12-001-x/2011002/article/11609-eng.pdf?st=5-sx8Q8n>.
The cube method is a probability sampling method that is designed to
satisfy criteria for balance between the sample and the population. Recent
research has shown that this method performs well in simulations for
studies of educational programs (see Fay & Olsen (2021, under review). To
implement the cube method, 'sitepickR' uses the sampling R package
<https://cran.r-project.org/package=sampling>. To implement statistical
matching, 'sitepickR' uses the 'MatchIt' R package
<https://cran.r-project.org/package=MatchIt>.

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
