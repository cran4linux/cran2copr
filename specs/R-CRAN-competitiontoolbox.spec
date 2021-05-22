%global packname  competitiontoolbox
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Graphical User Interface for Antitrust and Trade Practitioners

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-antitrust >= 0.99.11
BuildRequires:    R-CRAN-trade >= 0.5.4
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-rhandsontable 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-antitrust >= 0.99.11
Requires:         R-CRAN-trade >= 0.5.4
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-rhandsontable 
Requires:         R-CRAN-ggplot2 

%description
A graphical user interface for simulating the effects of mergers, tariffs,
and quotas under an assortment of different economic models. The interface
is powered by the 'Shiny' web application framework from 'RStudio'.

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
