%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  r5r
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Rapid Realistic Routing with 'R5'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-sf >= 1.0.12
BuildRequires:    R-CRAN-rJava >= 0.9.10
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-concaveman 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sfheaders 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zip 
Requires:         R-CRAN-sf >= 1.0.12
Requires:         R-CRAN-rJava >= 0.9.10
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-concaveman 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sfheaders 
Requires:         R-utils 
Requires:         R-CRAN-zip 

%description
Rapid realistic routing on multimodal transport networks (walk, bike,
public transport and car) using 'R5', the Rapid Realistic Routing on
Real-world and Reimagined networks engine
<https://github.com/conveyal/r5>. The package allows users to generate
detailed routing analysis or calculate travel time matrices using seamless
parallel computing on top of the R5 Java machine.  While R5 is developed
by Conveyal, the package r5r is independently developed by a team at the
Institute for Applied Economic Research (Ipea) with contributions from
collaborators. Apart from the documentation in this package, users will
find additional information on R5 documentation at
<https://docs.conveyal.com/>. Although we try to keep new releases of r5r
in synchrony with R5, the development of R5 follows Conveyal's independent
update process. Hence, users should confirm the R5 version implied by the
Conveyal user manual (see <https://docs.conveyal.com/changelog>)
corresponds with the R5 version that r5r depends on. This version of r5r
depends on R5 v7.1.

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
