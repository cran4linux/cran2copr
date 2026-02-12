%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OBIC
%global packver   4.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate the Open Bodem Index (OBI) Score

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-data.table 

%description
The Open Bodem Index (OBI) is a method to evaluate the quality of soils of
agricultural fields in The Netherlands and the sustainability of the
current agricultural practices. The OBI score is based on four main
criteria: chemical, physical, biological and management, which consist of
more than 21 indicators. By providing results of a soil analysis and
management info the 'OBIC' package can be use to calculate he scores,
indicators and derivatives that are used by the OBI. More information
about the Open Bodem Index can be found at <https://openbodemindex.nl/>.

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
