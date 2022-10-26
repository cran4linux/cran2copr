%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LOGAN
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Log File Analysis in International Large-Scale Assessments

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-psych >= 1.7.8
BuildRequires:    R-CRAN-foreign >= 0.8.69
BuildRequires:    R-CRAN-pander >= 0.6.1
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-modules 
BuildRequires:    R-methods 
Requires:         R-CRAN-psych >= 1.7.8
Requires:         R-CRAN-foreign >= 0.8.69
Requires:         R-CRAN-pander >= 0.6.1
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-modules 
Requires:         R-methods 

%description
Enables users to handle the dataset cleaning for conducting specific
analyses with the log files from two international educational
assessments: the Programme for International Student Assessment (PISA,
<https://www.oecd.org/pisa/>) and the Programme for the International
Assessment of Adult Competencies (PIAAC,
<https://www.oecd.org/skills/piaac/>). An illustration of the analyses can
be found on the LOGAN Shiny app
(<https://loganpackage.shinyapps.io/shiny/>) on your browser.

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
