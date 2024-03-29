%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AlleleShift
%global packver   1.1-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Predict and Visualize Population-Level Changes in Allele Frequencies in Response to Climate Change

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-vegan >= 2.6.4
BuildRequires:    R-CRAN-BiodiversityR >= 2.15.4
BuildRequires:    R-CRAN-adegenet 
Requires:         R-CRAN-vegan >= 2.6.4
Requires:         R-CRAN-BiodiversityR >= 2.15.4
Requires:         R-CRAN-adegenet 

%description
Methods (<doi:10.7717/peerj.11534>) are provided of calibrating and
predicting shifts in allele frequencies through redundancy analysis
('vegan::rda()') and generalized additive models ('mgcv::gam()').
Visualization functions for predicted changes in allele frequencies
include 'shift.dot.ggplot()', 'shift.pie.ggplot()', 'shift.moon.ggplot()',
'shift.waffle.ggplot()' and 'shift.surf.ggplot()' that are made with input
data sets that are prepared by helper functions for each visualization
method. Examples in the documentation show how to prepare animated climate
change graphics through a time series with the 'gganimate' package.
Function 'amova.rda()' shows how Analysis of Molecular Variance can be
directly conducted with the results from redundancy analysis.

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
