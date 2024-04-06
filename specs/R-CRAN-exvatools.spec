%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  exvatools
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          1%{?dist}%{?buildtag}
Summary:          Value Added in Exports and Other Input-Output Table Analysis Tools

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-data.table 
Requires:         R-methods 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-reshape2 
Requires:         R-utils 

%description
Analysis of trade in value added with international input-output tables.
Includes commands for easy data extraction, matrix manipulation,
decomposition of value added in gross exports and calculation of value
added indicators, with full geographical and sector customization.
Decomposition methods include Borin and Mancini (2023)
<doi:10.1080/09535314.2022.2153221>, Miroudot and Ye (2021)
<doi:10.1080/09535314.2020.1730308>, Wang et al. (2013)
<https://econpapers.repec.org/paper/nbrnberwo/19677.htm> and Koopman et
al. (2014) <doi:10.1257/aer.104.2.459>.

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
