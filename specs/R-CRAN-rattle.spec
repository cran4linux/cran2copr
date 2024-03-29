%global __brp_check_rpaths %{nil}
%global packname  rattle
%global packver   5.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Graphical User Interface for Data Science in R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-bitops 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-rpart.plot 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-bitops 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-rpart.plot 

%description
The R Analytic Tool To Learn Easily (Rattle) provides a collection of
utilities functions for the data scientist. A Gnome (RGtk2) based
graphical interface is included with the aim to provide a simple and
intuitive introduction to R for data science, allowing a user to quickly
load data from a CSV file (or via ODBC), transform and explore the data,
build and evaluate models, and export models as PMML (predictive modelling
markup language) or as scores. A key aspect of the GUI is that all R
commands are logged and commented through the log tab. This can be saved
as a standalone R script file and as an aid for the user to learn R or to
copy-and-paste directly into R itself. Note that RGtk2 and cairoDevice
have been archived on CRAN. See <https://rattle.togaware.com> for
installation instructions.

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
