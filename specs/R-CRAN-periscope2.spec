%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  periscope2
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Enterprise Streamlined 'shiny' Application Framework Using 'bs4Dash'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bs4Dash >= 2.3
BuildRequires:    R-CRAN-shiny >= 1.7
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-fresh 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-CRAN-shinyFeedback 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-bs4Dash >= 2.3
Requires:         R-CRAN-shiny >= 1.7
Requires:         R-CRAN-DT 
Requires:         R-CRAN-fresh 
Requires:         R-grDevices 
Requires:         R-CRAN-lubridate 
Requires:         R-methods 
Requires:         R-CRAN-miniUI 
Requires:         R-CRAN-shinyFeedback 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-utils 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-yaml 

%description
A framework for building enterprise, scalable and UI-standardized 'shiny'
applications. It brings enhanced features such as 'bootstrap' v4
<https://getbootstrap.com/docs/4.0/getting-started/introduction/>,
additional and enhanced 'shiny' modules, customizable UI features, as well
as an enhanced application file organization paradigm. This update allows
developers to harness the ability to build powerful applications and
enriches the 'shiny' developers' experience when building and maintaining
applications.

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
