%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  standardlastprofile
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          BDEW Standard Load Profiles for Electricity

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lifecycle 

%description
Provides representative standard load profiles (SLPs) for electricity
published by the German Association of Energy and Water Industries (BDEW
Bundesverband der Energie- und Wasserwirtschaft e.V.) in a tidy format.
Covers the 1999 profiles — households (H0), commerce (G0–G6), and
agriculture (L0–L2) — and the updated 2025 profiles (H25, G25, L25, P25,
S25), which additionally represent households with photovoltaic systems
and battery storage. Also provides an interface for generating a standard
load profile over a user-defined date range. The 1999 data and methodology
are described in VDEW (1999), "Repräsentative VDEW-Lastprofile",
<https://www.bdew.de/media/documents/1999_Repraesentative-VDEW-Lastprofile.pdf>.
The generation algorithm is described in VDEW (2000), "Anwendung der
Repräsentativen VDEW-Lastprofile step-by-step",
<https://www.bdew.de/media/documents/2000131_Anwendung-repraesentativen_Lastprofile-Step-by-step.pdf>.
The 2025 profiles are described in BDEW (2025), "Standardlastprofile
Strom", <https://www.bdew.de/energie/standardlastprofile-strom/>.

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
