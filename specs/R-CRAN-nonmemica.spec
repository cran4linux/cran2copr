%global packname  nonmemica
%global packver   0.9.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.7
Release:          1%{?dist}%{?buildtag}
Summary:          Create and Evaluate NONMEM Models in a Project Context

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.7.1
BuildRequires:    R-CRAN-metaplot >= 0.1.4
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-encode 
BuildRequires:    R-CRAN-csv 
BuildRequires:    R-CRAN-spec 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-dplyr >= 0.7.1
Requires:         R-CRAN-metaplot >= 0.1.4
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-encode 
Requires:         R-CRAN-csv 
Requires:         R-CRAN-spec 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 

%description
Systematically creates and modifies NONMEM(R) control streams. Harvests
NONMEM output, builds run logs, creates derivative data, generates
diagnostics. NONMEM (ICON Development Solutions <http://www.iconplc.com/>)
is software for nonlinear mixed effects modeling. See 'package?nonmemica'.

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
