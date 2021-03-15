%global packname  chlorpromazineR
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Convert Antipsychotic Doses to Chlorpromazine Equivalents

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch

%description
As different antipsychotic medications have different potencies, the doses
of different medications cannot be directly compared. Various strategies
are used to convert doses into a common reference so that comparison is
meaningful. Chlorpromazine (CPZ) has historically been used as a reference
medication into which other antipsychotic doses can be converted, as
"chlorpromazine-equivalent doses". Using conversion keys generated from
widely-cited scientific papers, e.g. Gardner et. al 2010
<doi:10.1176/appi.ajp.2009.09060802> and Leucht et al. 2016
<doi:10.1093/schbul/sbv167>, antipsychotic doses are converted to CPZ (or
any specified antipsychotic) equivalents. The use of the package is
described in the included vignette. Not for clinical use.

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
