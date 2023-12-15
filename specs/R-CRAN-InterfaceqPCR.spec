%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  InterfaceqPCR
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          GUI to Analyse qPCR Results after PMA Treatment or not

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-tkrplot 
BuildRequires:    R-CRAN-xlsx 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-reshape2 
Requires:         R-tcltk 
Requires:         R-CRAN-tkrplot 
Requires:         R-CRAN-xlsx 
Requires:         R-CRAN-plyr 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 

%description
Graphical User Interface allowing to determine the concentration in the
sample in CFU per mL or in number of copies per mL provided to qPCR
results after with or without PMA treatment. This package is simply to use
because no knowledge in R commands is necessary. A graphic represents the
standard curve, and a table containing the result for each sample is
created.

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
