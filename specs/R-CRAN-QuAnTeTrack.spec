%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  QuAnTeTrack
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Quantitative Analysis of Tetrapod Trackways

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-geomorph >= 4.0.3
BuildRequires:    R-CRAN-ggplot2 >= 3.3.6
BuildRequires:    R-CRAN-splancs >= 2.1.43
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-trajr >= 1.4.0
BuildRequires:    R-CRAN-SimilarityMeasures >= 1.4
BuildRequires:    R-CRAN-berryFunctions >= 1.21.14
BuildRequires:    R-CRAN-NISTunits >= 1.0.1
BuildRequires:    R-CRAN-ggrepel >= 0.9.1
BuildRequires:    R-CRAN-shotGroups >= 0.8.1
BuildRequires:    R-CRAN-schoolmath >= 0.4.1
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-dtw 
BuildRequires:    R-CRAN-dunn.test 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-mclust 
Requires:         R-CRAN-geomorph >= 4.0.3
Requires:         R-CRAN-ggplot2 >= 3.3.6
Requires:         R-CRAN-splancs >= 2.1.43
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-trajr >= 1.4.0
Requires:         R-CRAN-SimilarityMeasures >= 1.4
Requires:         R-CRAN-berryFunctions >= 1.21.14
Requires:         R-CRAN-NISTunits >= 1.0.1
Requires:         R-CRAN-ggrepel >= 0.9.1
Requires:         R-CRAN-shotGroups >= 0.8.1
Requires:         R-CRAN-schoolmath >= 0.4.1
Requires:         R-CRAN-car 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-dtw 
Requires:         R-CRAN-dunn.test 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-mclust 

%description
A quantitative and automated tool to extract (palaeo)biological
information (i.e., measurements, velocities, similarity metrics, etc.)
from the analysis of tetrapod trackways. Methods implemented in the
package draw from several sources, including Alexander (1976)
<doi:10.1038/261129a0>, Batschelet (1981, ISBN:9780120810505), Benhamou
(2004) <doi:10.1016/j.jtbi.2004.03.016>, Bovet and Benhamou (1988)
<doi:10.1016/S0022-5193(88)80038-9>, Cheung et al. (2007)
<doi:10.1007/s00422-007-0158-0>, Cheung et al. (2008)
<doi:10.1007/s00422-008-0251-z>, Cleasby et al. (2019)
<doi:10.1007/s00265-019-2761-1>, Farlow et al. (1981)
<doi:10.1038/294747a0>, Ostrom (1972) <doi:10.1016/0031-0182(72)90049-1>,
Rohlf (2008) <https://sbmorphometrics.org/>, Rohlf (2009)
<https://sbmorphometrics.org/>, Ruiz and Torices (2013)
<doi:10.1080/10420940.2012.759115>, Scrucca et al. (2016)
<doi:10.32614/RJ-2016-021>, Thulborn and Wade (1984)
<https://www.museum.qld.gov.au/collections-and-research/memoirs/nature-21/mqm-n21-2-11-thulborn-wade>.

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
