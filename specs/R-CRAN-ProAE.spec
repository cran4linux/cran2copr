%global packname  ProAE
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          PRO-CTCAE Data Management, Analysis, and Graphical Tools

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggnewscale 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggnewscale 
Requires:         R-CRAN-ggtext 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-magrittr 

%description
A collection of tools to facilitate standardized analysis and graphical
procedures when using the National Cancer Institute’s Patient-Reported
Outcomes version of the Common Terminology Criteria for Adverse Events
(PRO-CTCAE).

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
