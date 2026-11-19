%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rapsimng.decide
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Decision-Oriented Analysis Interface for APSIM Next Generation Outputs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rapsimng 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rapsimng.decide.core 
BuildRequires:    R-CRAN-rapsimng.decide.cultivar 
BuildRequires:    R-CRAN-rapsimng.decide.sowing 
BuildRequires:    R-CRAN-rapsimng.decide.nitrogen 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rapsimng 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rapsimng.decide.core 
Requires:         R-CRAN-rapsimng.decide.cultivar 
Requires:         R-CRAN-rapsimng.decide.sowing 
Requires:         R-CRAN-rapsimng.decide.nitrogen 

%description
Provides a high-level interface for analysing Agricultural Production
Systems sIMulator ('APSIM') Next Generation simulation outputs to support
structured decision-making workflows. The package coordinates
domain-specific decision modules (e.g. cultivar selection, experimental
design) and standardises their outputs into reproducible decision reports.
It does not perform 'APSIM' simulations or implement decision logic
directly, but serves as an orchestration layer connecting analysis results
with reporting and downstream interpretation.

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
