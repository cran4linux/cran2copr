%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RoME
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Multiple Checks on MEDITS Trawl Survey Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-timeDate 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rnaturalearth 
BuildRequires:    R-CRAN-rnaturalearthdata 
BuildRequires:    R-CRAN-zip 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-timeDate 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rnaturalearth 
Requires:         R-CRAN-rnaturalearthdata 
Requires:         R-CRAN-zip 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-shiny 

%description
Provides quality checks for MEDITS (International Bottom Trawl Survey in
the Mediterranean) trawl survey exchange data tables (TA (Haul data), TB
(Catch data), TC (Biological data), TE (Biological individual data), TL
(Litter data)). The main function RoME() calls all check functions in a
defined sequence to perform a complete quality control of TX (Generic
exchange data) data, including header validation, controlled-vocabulary
checks, cross-table consistency tests, and biological plausibility checks.
No automatic correction is applied: the package detects errors, warns the
user, and specifies the type of error to ease data correction. Checks can
be run simultaneously on multi-year datasets. An embedded 'shiny'
application is also provided via run_RoME_app(). References describing the
methods: MEDITS Working Group (2017)
<https://www.sibm.it/MEDITS%%202011/principaledownload.htm>.

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
