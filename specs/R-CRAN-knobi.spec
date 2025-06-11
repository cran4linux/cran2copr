%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  knobi
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Known-Biomass Production Model (KBPM)

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-grDevices 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-plot3D 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 

%description
Application of a Known Biomass Production Model (KBPM): (1) the fitting of
KBPM to each stock; (2) the estimation of the effects of environmental
variability; (3) the retrospective analysis to identify regime shifts; (4)
the estimation of forecasts. For more details see Schaefer (1954)
<https://www.iattc.org/GetAttachment/62d510ee-13d0-40f2-847b-0fde415476b8/Vol-1-No-2-1954-SCHAEFER,-MILNER-B-_Some-aspects-of-the-dynamics-of-populations-important-to-the-management-of-the-commercial-marine-fisheries.pdf>,
Pella and Tomlinson (1969)
<https://www.iattc.org/GetAttachment/9865079c-6ee7-40e2-9e30-c4523ff81ddf/Vol-13-No-3-1969-PELLA,-JEROME-J-,-and-PATRICK-K-TOMLINSON_A-generalized-stock-production-model.pdf>
and MacCall (2002)
<doi:10.1577/1548-8675(2002)022%%3C0272:UOKBPM%%3E2.0.CO;2>.

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
