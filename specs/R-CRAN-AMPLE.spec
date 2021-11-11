%global __brp_check_rpaths %{nil}
%global packname  AMPLE
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Shiny Apps to Support Capacity Building on Harvest Control Rules

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-R6 >= 2.5.1
BuildRequires:    R-CRAN-shinyjs >= 2.0.0
BuildRequires:    R-CRAN-shiny >= 1.7.1
BuildRequires:    R-CRAN-scales >= 1.1.1
BuildRequires:    R-CRAN-shinyscreenshot >= 0.1.0
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-R6 >= 2.5.1
Requires:         R-CRAN-shinyjs >= 2.0.0
Requires:         R-CRAN-shiny >= 1.7.1
Requires:         R-CRAN-scales >= 1.1.1
Requires:         R-CRAN-shinyscreenshot >= 0.1.0
Requires:         R-CRAN-markdown 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-stats 

%description
Three Shiny apps are provided that introduce Harvest Control Rules (HCR)
for fisheries management. 'Introduction to HCRs' provides a simple
overview to how HCRs work. Users are able to select their own HCR and step
through its performance, year by year. Biological variability and
estimation uncertainty are introduced. 'Measuring performance' builds on
the previous app and introduces the idea of using performance indicators
to measure HCR performance. 'Comparing performance' allows multiple HCRs
to be created and tested, and their performance compared so that the
preferred HCR can be selected.

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
