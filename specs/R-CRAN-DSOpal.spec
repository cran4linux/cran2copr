%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DSOpal
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          'DataSHIELD' Implementation for 'Opal'

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-opalr >= 3.0
BuildRequires:    R-CRAN-DSI >= 1.5
BuildRequires:    R-methods 
Requires:         R-CRAN-opalr >= 3.0
Requires:         R-CRAN-DSI >= 1.5
Requires:         R-methods 

%description
'DataSHIELD' is an infrastructure and series of R packages that enables
the remote and 'non-disclosive' analysis of sensitive research data. This
package is the 'DataSHIELD' interface implementation for 'Opal', which is
the data integration application for biobanks by 'OBiBa'. Participant
data, once collected from any data source, must be integrated and stored
in a central data repository under a uniform model. 'Opal' is such a
central repository. It can import, process, validate, query, analyze,
report, and export data. 'Opal' is the reference implementation of the
'DataSHIELD' infrastructure.

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
