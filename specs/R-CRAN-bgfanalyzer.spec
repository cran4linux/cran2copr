%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bgfanalyzer
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analyze Microbial Biogas Fermentation Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-dplyr 
Requires:         R-graphics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 

%description
Provides a new S3 class object and relevant methods to analyze biogas
fermentation data. It includes three workflows. One is specialized to a
commercially available lab-scale fermentation system (see e.g. Nwaigwe
(2018) <doi:10.1115/ES2018-7553>). The second provides more flexibility
and allows to import data from plain text files. The last workflow offers
the most flexibility as it doesn't expect external input files but relays
on interactive user input. Although the focus is set on biogas
fermentations, concepts and workflows may be also applicable to other
fermentations even if not a gaseous product is measured. Furthermore, it
provides functions that bridge to established plot engines (e.g. 'ggplot2'
or 'plotly') for data visualisation. 'bgfanalyzer' catches up an idea of
Hafner et al. (2018) <doi:10.1016/j.softx.2018.06.005> of using R to
standardize research within the biogas field. For more details on
standardization efforts within the biogas research field see Hollinger et
al. (2016) <doi:10.2166/wst.2016.336> and Hollinger et al. (2021)
<doi:10.2166/wst.2020.569>.

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
