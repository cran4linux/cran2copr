%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  WrightMap
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          IRT Item-Person Map with 'ConQuest' Integration

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-methods 
Requires:         R-CRAN-RColorBrewer 

%description
A powerful yet simple graphical tool available in the field of
psychometrics is the Wright Map (also known as item maps or item-person
maps), which presents the location of both respondents and items on the
same scale. Wright Maps are commonly used to present the results of
dichotomous or polytomous item response models. The 'WrightMap' package
provides functions to create these plots from item parameters and person
estimates stored as R objects. Although the package can be used in
conjunction with any software used to estimate the IRT model (e.g. 'TAM',
'mirt', 'eRm' or 'IRToys' in 'R', or 'Stata', 'Mplus', etc.), 'WrightMap'
features special integration with 'ConQuest' to facilitate reading and
plotting its output directly.The 'wrightMap' function creates Wright Maps
based on person estimates and item parameters produced by an item response
analysis. The 'CQmodel' function reads output files created using
'ConQuest' software and creates a set of data frames for easy data
manipulation, bundled in a 'CQmodel' object. The 'wrightMap' function can
take a 'CQmodel' object as input or it can be used to create Wright Maps
directly from data frames of person and item parameters.

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
