%global packname  rPraat
%global packver   1.3.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to Praat

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-graphics >= 3.1.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-tuneR >= 1.3.3
BuildRequires:    R-CRAN-readr >= 1.3.1
BuildRequires:    R-CRAN-dygraphs >= 1.1.1.6
BuildRequires:    R-CRAN-dplyr >= 0.8.5
Requires:         R-graphics >= 3.1.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-tuneR >= 1.3.3
Requires:         R-CRAN-readr >= 1.3.1
Requires:         R-CRAN-dygraphs >= 1.1.1.6
Requires:         R-CRAN-dplyr >= 0.8.5

%description
Read, write and manipulate 'Praat' TextGrid, PitchTier, Pitch,
IntensityTier, Formant, Sound, and Collection files
<https://www.fon.hum.uva.nl/praat/>.

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
