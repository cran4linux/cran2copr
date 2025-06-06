%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  surveytable
%global packver   0.9.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.8
Release:          1%{?dist}%{?buildtag}
Summary:          Formatted Survey Estimates

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-huxtable 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-huxtable 

%description
Short and understandable commands that generate tabulated, formatted, and
rounded survey estimates. Mostly a wrapper for the 'survey' package
(Lumley (2004) <doi:10.18637/jss.v009.i08>
<https://CRAN.R-project.org/package=survey>) that identifies low-precision
estimates using the National Center for Health Statistics (NCHS)
presentation standards (Parker et al. (2017)
<https://www.cdc.gov/nchs/data/series/sr_02/sr02_175.pdf>, Parker et al.
(2023) <doi:10.15620/cdc:124368>).

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
