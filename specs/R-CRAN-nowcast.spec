%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nowcast
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Economic Nowcasting with Bridge Equations and Real-Time Evaluation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 

%description
Provides bridge equations with optional autoregressive terms for
nowcasting low-frequency macroeconomic variables (e.g. quarterly GDP) from
higher-frequency indicators (e.g. monthly retail sales). Handles the
ragged-edge problem where different indicators have different publication
lags via mixed-frequency alignment. Includes pseudo-real-time evaluation
with expanding or rolling windows, and the Diebold-Mariano test for
comparing forecast accuracy following Harvey, Leybourne, and Newbold
(1997) <doi:10.1016/S0169-2070(96)00719-4>. No API calls; designed to work
with data from any source.

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
