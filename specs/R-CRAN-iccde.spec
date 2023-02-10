%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  iccde
%global packver   0.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.5
Release:          1%{?dist}%{?buildtag}
Summary:          Computation of the Double-Entry Intraclass Correlation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
The functions compute the double-entry intraclass correlation, which is an
index of profile similarity (Furr, 2010; McCrae, 2008). The double-entry
intraclass correlation is a more precise index of the agreement of two
empirically observed profiles than the often-used intraclass correlation
(McCrae, 2008). The function transforms profiles comprising correlations
according to the Fisher z-transformation before the double-entry
intraclass correlation is calculated. If the profiles comprise scores such
as sum scores from various personality scales, it is recommended to
standardize each individual score prior to computation of the double-entry
intraclass correlation (McCrae, 2008). See Furr (2010)
<doi:10.1080/00223890903379134> or McCrae (2008)
<doi:10.1080/00223890701845104> for details.

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
