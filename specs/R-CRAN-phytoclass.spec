%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  phytoclass
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate Chla Concentrations of Phytoplankton Groups

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.8
Requires:         R-core >= 3.8
BuildArch:        noarch
BuildRequires:    R-CRAN-bestNormalize 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-dynamicTreeCut 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-CRAN-RcppML 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-bestNormalize 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-dynamicTreeCut 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Metrics 
Requires:         R-CRAN-RcppML 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 

%description
Determine the chlorophyll a (Chl a) concentrations of different
phytoplankton groups based on their pigment biomarkers. The method uses
non-negative matrix factorisation and simulated annealing to minimise
error between the observed and estimated values of pigment concentrations
(Hayward et al. (2023) <doi:10.1002/lom3.10541>). The approach is similar
to the widely used 'CHEMTAX' program (Mackey et al. 1996)
<doi:10.3354/meps144265>, but is more straightforward, accurate, and not
reliant on initial guesses for the pigment to Chl a ratios for
phytoplankton groups.

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
