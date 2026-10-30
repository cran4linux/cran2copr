%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  datagrade
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Data Quality Assessment on the ISO/IEC 25012 Model

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-cli 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
A single-call data quality assessment scoring a data set on the five
inherent characteristics of the ISO/IEC 25012 data quality model
(accuracy, completeness, consistency, credibility and currentness) through
the fifteen quality properties beneath them, ISO/IEC (2008)
<https://www.iso.org/standard/35736.html>. Each property is measured as a
ratio of counted data items, the form ISO/IEC 25024 measurement functions
take, ISO/IEC (2015) <https://www.iso.org/standard/35749.html>. Six
properties are computable from a table alone; the rest compare the data
against expectations declared through a specification object, and are
reported as not applicable rather than approximated when none is supplied.
Also reports missing-data patterns, duplicates, redundant columns,
outliers, multicollinearity and distributional deviations, and returns a
structured object with plots rather than console text alone. The
statistics implement the methodology of the author's master's
dissertation, Demirhan (2024) "Assessing Data Quality Management Issues in
Open-Sourced Data Sets with Statistical Methodology"
<https://halukdemirhan.com/assets/msc-thesis-haluk-demirhan-public.pdf>.

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
