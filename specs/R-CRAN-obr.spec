%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  obr
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Access 'Office for Budget Responsibility' Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-tools 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-readxl 
Requires:         R-tools 

%description
Provides clean, tidy access to data published by the 'Office for Budget
Responsibility' ('OBR'), the UK's independent fiscal watchdog. Covers the
Public Finances Databank (outturn for PSNB, PSND, receipts, and
expenditure since 1946), the Historical Official Forecasts Database (every
'OBR' forecast since 2010), the Economic and Fiscal Outlook detailed
forecast tables (five-year projections from the latest Budget), the
Welfare Trends Report (incapacity benefit spending and caseloads), and the
Fiscal Risks and Sustainability Report (50-year state pension
projections). Data is downloaded from the 'OBR' on first use and cached
locally for subsequent calls. Data is sourced from the 'OBR' website
<https://obr.uk>.

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
