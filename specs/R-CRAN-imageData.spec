%global packname  imageData
%global packver   0.1-61
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.61
Release:          1%{?dist}%{?buildtag}
Summary:          Aids in Processing and Plotting Data from a Lemna-Tec Scananalyzer

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dae 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-grid 
Requires:         R-CRAN-dae 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-reshape 
Requires:         R-grid 

%description
Note that 'imageData' has been superseded by 'growthPheno'. The package
'growthPheno' incorporates all the functionality of 'imageData' and has
functionality not available in 'imageData', but some 'imageData' functions
have been renamed. The 'imageData' package is no longer maintained, but is
retained for legacy purposes.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
