%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rintcal
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Radiocarbon Calibration Curves

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-jsonlite 

%description
The IntCal20 radiocarbon calibration curves (Reimer et al. 2020
<doi:10.1017/RDC.2020.68>) are provided as a data package, together with
previous IntCal curves (IntCal13, IntCal09, IntCal04, IntCal98), other
curves (e.g., NOTCal04 [van der Plicht et al. 2004], Arnold & Libby 1951,
Stuiver & Suess 1966, Pearson & Stuiver 1986) and postbomb curves. Also
provided are functions to copy the curves into memory, and to read, query
and plot the data underlying the IntCal20 curves.

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
