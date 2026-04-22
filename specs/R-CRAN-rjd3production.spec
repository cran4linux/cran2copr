%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rjd3production
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Prepare for Production of Seasonal Adjustment with 'JDemetra+'

License:          EUPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rjd3toolkit 
BuildRequires:    R-CRAN-rjd3x13 
BuildRequires:    R-CRAN-rjd3workspace 
BuildRequires:    R-CRAN-rjd3providers 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-dygraphs 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-constructive 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-TBox 
BuildRequires:    R-CRAN-date4ts 
BuildRequires:    R-CRAN-lintr 
Requires:         R-CRAN-rjd3toolkit 
Requires:         R-CRAN-rjd3x13 
Requires:         R-CRAN-rjd3workspace 
Requires:         R-CRAN-rjd3providers 
Requires:         R-utils 
Requires:         R-CRAN-dygraphs 
Requires:         R-CRAN-flextable 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-tools 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-constructive 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-TBox 
Requires:         R-CRAN-date4ts 
Requires:         R-CRAN-lintr 

%description
A comprehensive tool for setting up seasonal data pipelines using
'JDemetra+' (version 3) and 'rjdverse'. This includes setting up a new
working environment, creating and selecting calendar regressors, managing
specifications (trading-days regressors and outliers) at the workspace
level, making a workspace usable by the 'cruncher', removing insignificant
outliers, and comparing workspaces.

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
