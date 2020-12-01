%global packname  r5r
%global packver   0.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Rapid Realistic Routing with 'R5'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-sf >= 0.9.3
BuildRequires:    R-CRAN-rJava >= 0.9.10
BuildRequires:    R-CRAN-jdx >= 0.1.4
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sfheaders 
BuildRequires:    R-utils 
Requires:         R-CRAN-sf >= 0.9.3
Requires:         R-CRAN-rJava >= 0.9.10
Requires:         R-CRAN-jdx >= 0.1.4
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-data.table 
Requires:         R-methods 
Requires:         R-CRAN-sfheaders 
Requires:         R-utils 

%description
Rapid realistic routing on multimodal transport networks (walk, bike,
public transport and car) using 'R5', the Rapid Realistic Routing on
Real-world and Reimagined networks <https://github.com/conveyal/r5>. The
package allows users to generate detailed routing analysis or calculate
travel time matrices using seamless parallel computing on top of the R5
Java machine.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
