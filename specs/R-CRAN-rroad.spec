%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rroad
%global packver   0.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Road Condition Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Computation of the International Roughness Index (IRI) given a
longitudinal road profile. The IRI can be calculated for a single road
segment or for a sequence of segments with a fixed length (e. g. 100m).
For the latter, an overlap of the segments can be selected. The IRI and
likewise the algorithms for its determination are defined in Sayers,
Michael W; Gillespie, Thomas D; Queiroz, Cesar A.V. 1986. The
International Road Roughness Experiment (IRRE) : establishing correlation
and a calibration standard for measurements. World Bank technical paper;
no. WTP 45. Washington, DC : The World Bank. (ISBN 0-8213-0589-1)
available from
<http://documents.worldbank.org/curated/en/326081468740204115>.

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
