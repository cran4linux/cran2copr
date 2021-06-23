%global __brp_check_rpaths %{nil}
%global packname  aoristic
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generates Aoristic Probability Distributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 

%description
It can sometimes be difficult to ascertain when some events (such as
property crime) occur because the victim is not present when the crime
happens. As a result, police databases often record a 'start' (or 'from')
date and time, and an 'end' (or 'to') date and time. The time span between
these date/times can be minutes, hours, or sometimes days, hence the term
'Aoristic'. Aoristic is one of the past tenses in Greek and represents an
uncertain occurrence in time. For events with a location describes with
either a latitude/longitude, or X,Y coordinate pair, and a start and end
date/time, this package generates an aoristic data frame with aoristic
weighted probability values for each hour of the week, for each
observation. The coordinates are not necessary for the program to
calculate aoristic weights; however, they are part of this package because
a spatial component has been integral to aoristic analysis from the start.
Dummy coordinates can be introduced if the user only has temporal data.
Outputs include an aoristic data frame, as well as summary graphs and
displays. For more information see: Ratcliffe, JH (2002) Aoristic
signatures and the temporal analysis of high volume crime patterns,
Journal of Quantitative Criminology. 18 (1): 23-43. Note: This package
replaces an original 'aoristic' package (version 0.6) by George Kikuchi
that has been discontinued with his permission.

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
