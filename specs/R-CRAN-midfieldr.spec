%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  midfieldr
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Tools and Methods for Working with MIDFIELD Data in 'R'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.9.8
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-wrapr 
Requires:         R-CRAN-data.table >= 1.9.8
Requires:         R-CRAN-checkmate 
Requires:         R-stats 
Requires:         R-CRAN-wrapr 

%description
Provides tools and demonstrates methods for working with individual
undergraduate student-level records (registrar's data) in 'R'. Tools
include filters for program codes, data sufficiency, and timely
completion. Methods include gathering blocs of records, computing
quantitative metrics such as graduation rate, and creating charts to
visualize comparisons. 'midfieldr' interacts with practice data provided
in 'midfielddata', an R data package available at
<https://midfieldr.github.io/midfielddata/>. 'midfieldr' also interacts
with the full MIDFIELD database for users who have access. This work is
supported by the US National Science Foundation through grant numbers
1545667 and 2142087.

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
