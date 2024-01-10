%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EWSmethods
%global packver   1.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Forecasting Tipping Points at the Community Level

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-rEDM >= 1.15.0
BuildRequires:    R-CRAN-dplyr >= 1.0.6
BuildRequires:    R-CRAN-egg 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-infotheo 
BuildRequires:    R-CRAN-mAr 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-rEDM >= 1.15.0
Requires:         R-CRAN-dplyr >= 1.0.6
Requires:         R-CRAN-egg 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-infotheo 
Requires:         R-CRAN-mAr 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-zoo 

%description
Rolling and expanding window approaches to assessing abundance based early
warning signals, non-equilibrium resilience measures, and machine
learning. See Dakos et al. (2012) <doi:10.1371/journal.pone.0041010>, Deb
et al. (2022) <doi:10.1098/rsos.211475>, Drake and Griffen (2010)
<doi:10.1038/nature09389>, Ushio et al. (2018) <doi:10.1038/nature25504>
and Weinans et al. (2021) <doi:10.1038/s41598-021-87839-y> for
methodological details. Graphical presentation of the outputs are also
provided for clear and publishable figures. Visit the 'EWSmethods' website
for more information, and tutorials.

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
