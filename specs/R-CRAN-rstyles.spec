%global __brp_check_rpaths %{nil}
%global packname  rstyles
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generating Simulated Data Mimicking Response Styles to Survey Questions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch

%description
Package allows to generate simulated datasets using algorithms that mimic
different response styles to survey questions using: 1) IRTree approach
(Bockenholt (2012) <doi:10.1037/a0028111>, (2017)
<doi:10.1037/met0000106>), 2) (G)PCM (and rating scale version of a
partial credit model) random-thresholds approach (Falk & Cai (2016)
<doi:10.1037/met0000059>; Henninger & Meiser (2020a)
<doi:10.1037/met0000249>, (2020b) <doi:10.1037/met0000268>; Plieninger
(2017) <doi:10.1177/0013164416636655>), 3) user provided function that
(with some probability) chooses response using information about previous
responses. This allows to cover wide range of potential response styles
like: extreme and middle (ERS, MRS), acquiesce (ARS) and also
careless/inattentive responding (CR, IR).

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
