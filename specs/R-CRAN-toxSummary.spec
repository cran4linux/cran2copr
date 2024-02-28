%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  toxSummary
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Visualize and Summarize Repeat-Dose Toxicology Study Results

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-cicerone 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-ggiraph 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-shinydisconnect 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-cicerone 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-ggiraph 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-shinydisconnect 
Requires:         R-CRAN-stringr 

%description
A 'shiny' app that generates plots and summary tables from repeat-dose
toxicology study results to facilitate holistic evaluation of the drug
safety of active pharmaceutical ingredients (API) prior to initiation of
clinical trials.

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
