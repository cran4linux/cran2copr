%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tipitaka.critical
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Lemmatized Critical Edition of the Pali Canon

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-Matrix 

%description
A lemmatized critical edition of the complete Pali Canon (Tipitaka), the
canonical scripture of Theravadin Buddhism. Based on a five-witness
collation of the Pali Text Society (PTS) edition (via 'GRETIL'),
'SuttaCentral', the Vipassana Research Institute (VRI) Chattha Sangayana
edition, the Buddha Jayanti Tipitaka (BJT), and the Thai Royal Edition.
All text is lemmatized using the 'Digital Pali Dictionary', grouping
inflected forms by dictionary headword. Covers all three pitakas (Sutta,
Vinaya, Abhidhamma) with 5,777 individual text units. The companion
package 'tipitaka' provides the original VRI edition data and Pali text
tools. For background on the collation method, see Zigmond (2026)
<https://github.com/dangerzig/tipitaka.critical>.

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
