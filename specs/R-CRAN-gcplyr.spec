%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gcplyr
%global packver   1.13.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.13.1
Release:          1%{?dist}%{?buildtag}
Summary:          Wrangle and Analyze Growth Curve Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-tools 
Requires:         R-utils 

%description
Easy importing, wrangling, and model-free analysis of microbial growth
curve data, as commonly output by plate readers. Tools for flexibly
importing all the common data formats output by plate readers and
reshaping them into 'tidy' formats for analyses. Tools for importing
experimental designs from files or generating them in R and merging design
information with density data, making it easy to analyze with 'gcplyr' and
'tidyverse' or 'dplyr' functions, and to plot with 'ggplot2'. Streamlines
extracting parameters like growth rate/doubling time, maximum density
(carrying capacity), lag time, area under the curve, diauxic shifts,
extinction, and more without fitting an equation for growth to your data.
Has several methods to deal with noise in growth curve data. See methods
at <https://mikeblazanin.github.io/gcplyr/>.

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
