%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FAfA
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Factor Analysis for All

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-golem 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-psych 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-utils 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-golem 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-psych 

%description
This Shiny application offers researchers a comprehensive tool for
performing factor analysis. Users can upload datasets, validate
assumptions, manage missing and outlier data, split data for different
analyses, and run exploratory and confirmatory factor analyses ("EFA" and
"CFA"). The software also offers reliability analysis, exploratory graph
analysis, and item weighting. With a user-friendly interface, this tool
simplifies the EFA and CFA processes. The main features are data
submission and simple data inspection. Data manipulation (excluding
variables, splitting data, checking for outliers), assumption checking
(Tabachnik & Fidell (2012) <ISBN:978-0-205-84957-4> and Field (2009)
<ISBN:978-1-84787-906-6>) for factor analysis, exploratory factor analysis
(with various factor number determination methods (Lorenzo-Seva & Ferrando
(2021) <doi:10.5964/meth.7185>)), confirmatory factor analysis (model
definition and modification suggestions (Kline (2011)
<ISBN:978-1-60623-877-6>)), reliability analysis (Cronbach's alpha,
McDonald's omega, Armor's theta, structural reliability, stratified
alpha), item weighting (Kilic & Dogan (2019) <doi:10.21031/epod.516057>).

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
