%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  insane
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          INsulin Secretion ANalysEr

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggthemes >= 4.2.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.2
BuildRequires:    R-CRAN-shiny >= 1.5.0
BuildRequires:    R-CRAN-glue >= 1.4.1
BuildRequires:    R-CRAN-readxl >= 1.3.1
BuildRequires:    R-CRAN-tidyr >= 1.1.0
BuildRequires:    R-CRAN-patchwork >= 1.0.1
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-ggbeeswarm >= 0.6.0
BuildRequires:    R-CRAN-broom >= 0.5.6
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-ggpubr >= 0.3.0
BuildRequires:    R-CRAN-DT >= 0.13
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggthemes >= 4.2.0
Requires:         R-CRAN-ggplot2 >= 3.3.2
Requires:         R-CRAN-shiny >= 1.5.0
Requires:         R-CRAN-glue >= 1.4.1
Requires:         R-CRAN-readxl >= 1.3.1
Requires:         R-CRAN-tidyr >= 1.1.0
Requires:         R-CRAN-patchwork >= 1.0.1
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-ggbeeswarm >= 0.6.0
Requires:         R-CRAN-broom >= 0.5.6
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-ggpubr >= 0.3.0
Requires:         R-CRAN-DT >= 0.13
Requires:         R-stats 
Requires:         R-utils 

%description
A user-friendly interface, using Shiny, to analyse glucose-stimulated
insulin secretion (GSIS) assays in pancreatic beta cells or islets. The
package allows the user to import several sets of experiments from
different spreadsheets and to perform subsequent steps: summarise in a
tidy format, visualise data quality and compare experimental conditions
without omitting to account for technical confounders such as the date of
the experiment or the technician. Together, insane is a comprehensive
method that optimises pre-processing and analyses of GSIS experiments in a
friendly-user interface. The Shiny App was initially designed for
EndoC-betaH1 cell line following method described in Ndiaye et al., 2017
(<doi:10.1016/j.molmet.2017.03.011>).

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
