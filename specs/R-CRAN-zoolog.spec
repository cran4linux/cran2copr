%global __brp_check_rpaths %{nil}
%global packname  zoolog
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Zooarchaeological Analysis with Log-Ratios

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack >= 0.7
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-Rdpack >= 0.7
Requires:         R-utils 
Requires:         R-CRAN-stringi 

%description
Includes functions and reference data to generate and manipulate
log-ratios (also known as log size index (LSI) values) from measurements
obtained on zooarchaeological material. Log ratios are used to compare the
relative (rather than the absolute) dimensions of animals from
archaeological contexts (Meadow 1999, ISBN: 9783896463883). zoolog is also
able to seamlessly integrate data and references with heterogeneous
nomenclature, which is internally managed by a zoolog thesaurus. A
preliminary version of the zoolog methods was first used by Trentacoste,
Nieto-Espinet, and Valenzuela-Lamas (2018)
<doi:10.1371/journal.pone.0208109>.

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
