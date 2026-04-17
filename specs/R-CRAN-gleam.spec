%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gleam
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          1%{?dist}%{?buildtag}
Summary:          Global Livestock Environmental Assessment Model (GLEAM-X)

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-CRAN-data.table >= 1.16.0
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-data.table >= 1.16.0

%description
The official implementation of the Global Livestock Environmental
Assessment Model (GLEAM) of the Food and Agriculture Organization of the
United Nations (FAO) in R. GLEAM-X provides a modular, transparent
framework for simulating livestock production systems and quantifying
their environmental impacts. Methodological background: MacLeod et al.
(2017) "Invited review: A position on the Global Livestock Environmental
Assessment Model (GLEAM)" <doi:10.1017/S1751731117001847>. Further
information: <https://www.fao.org/gleam/en/>.

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
