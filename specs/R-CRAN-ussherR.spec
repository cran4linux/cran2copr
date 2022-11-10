%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ussherR
%global packver   1.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.10
Release:          1%{?dist}%{?buildtag}
Summary:          Ussher Data Set Drawn from 1658 Chronology

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
The "ussher" data set is drawn from original chronological textual
historic events. Commonly known as James Ussher's Annals of the World, the
source text was originally written in Latin in 1650, and published in
English translation in 1658.The data are classified by index, year, epoch
(or one of the 7 ancient "Ages of the World"), Biblical source book if
referenced (rarely), as well as alternate dating mechanisms, such as "Anno
Mundi" (age of the world) or "Julian Period" (dates based upon the Julian
calendar). Additional file "usshfull" includes variables that may be of
further interest to historians, such as Southern Kingdom and Northern
Kingdom discrepant dates, and the original amalgamated dating mechanic
used by Ussher in the original text. The raw data can also be called using
"usshraw", as described in: Ussher, J. (1658)
<https://archive.org/stream/AnnalsOfTheWorld/Annals_djvu.txt>.

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
