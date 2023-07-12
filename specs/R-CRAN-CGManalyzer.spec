%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CGManalyzer
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Continuous Glucose Monitoring Data Analyzer

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Contains all of the functions necessary for the complete analysis of a
continuous glucose monitoring study and can be applied to data measured by
various existing 'CGM' devices such as 'FreeStyle Libre', 'Glutalor',
'Dexcom' and 'Medtronic CGM'. It reads a series of data files, is able to
convert various formats of time stamps, can deal with missing values,
calculates both regular statistics and nonlinear statistics, and conducts
group comparison. It also displays results in a concise format. Also
contains two unique features new to 'CGM' analysis: one is the
implementation of strictly standard mean difference and the class of
effect size; the other is the development of a new type of plot called
antenna plot. It corresponds to 'Zhang
XD'(2018)<doi:10.1093/bioinformatics/btx826>'s article 'CGManalyzer: an R
package for analyzing continuous glucose monitoring studies'.

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
