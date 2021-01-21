%global packname  ITGM
%global packver   0.42
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.42
Release:          1%{?dist}%{?buildtag}
Summary:          Individual Tree Growth Modeling

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Fgmutils >= 0.8
BuildRequires:    R-CRAN-gsubfn 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-sqldf 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-randomcoloR 
BuildRequires:    R-CRAN-rbokeh 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-Fgmutils >= 0.8
Requires:         R-CRAN-gsubfn 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-sqldf 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-randomcoloR 
Requires:         R-CRAN-rbokeh 
Requires:         R-CRAN-ggplot2 

%description
Individual tree model is an instrument to support the decision with regard
to forest management. This package provides functions that let you work
with data for this model. Also other support functions and extension
related to this model are available.

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
