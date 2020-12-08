%global packname  clickR
%global packver   0.5.27
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.27
Release:          1%{?dist}%{?buildtag}
Summary:          Fix Data and Create Report Tables from Different Objects

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-beeswarm 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-xtable 
Requires:         R-CRAN-beeswarm 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-lmerTest 
Requires:         R-methods 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-xtable 

%description
Tools for assessing data quality, performing exploratory analysis, fixing
data errors in numerical, factor and date variables and creating report
tables from models and summaries.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
