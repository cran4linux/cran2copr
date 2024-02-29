%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  saros
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Semi-Automatic Reporting of Ordinary Surveys

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-bcrypt 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggiraph 
BuildRequires:    R-CRAN-mschart 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-clipr 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-rvest 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-bcrypt 
Requires:         R-utils 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggiraph 
Requires:         R-CRAN-mschart 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-clipr 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-rvest 

%description
Produces highly customized reports, primarily intended for survey
research. Building on 'Quarto' (<https://quarto.org>), it generates draft
chapters of all specified dependent/independent variables, which can be
further edited by hand, containing figures, tables and analyses (currently
only uni-/bivariate tests of equivalent means/proportions). The feature
'mesos'-reports offer tailor-made batch report production where e.g. an
institution can compare itself to all other participants. Publication
tools are also included, such as password generation for 'mesos'-report
sections on a 'Quarto' Website.

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
