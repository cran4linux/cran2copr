%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  edibble
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Encapsulating Elements of Experimental Design

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-pillar 
BuildRequires:    R-CRAN-nestr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-AlgDesign 
BuildRequires:    R-CRAN-dae 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-pillar 
Requires:         R-CRAN-nestr 
Requires:         R-stats 
Requires:         R-CRAN-AlgDesign 
Requires:         R-CRAN-dae 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-dplyr 

%description
A system to facilitate designing comparative (and non-comparative)
experiments using the grammar of experimental designs
<https://emitanaka.org/edibble-book/>. An experimental design is treated
as an intermediate, mutable object that is built progressively by
fundamental experimental components like units, treatments, and their
relation. The system aids in experimental planning, management and
workflow.

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
