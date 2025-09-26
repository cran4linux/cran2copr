%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  inTextSummaryTable
%global packver   3.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3.5
Release:          1%{?dist}%{?buildtag}
Summary:          Creation of in-Text Summary Table

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Recommends:       pandoc
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-reshape2 >= 1.4
BuildRequires:    R-CRAN-flextable >= 0.5.5
BuildRequires:    R-CRAN-clinUtils >= 0.1.0
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-reshape2 >= 1.4
Requires:         R-CRAN-flextable >= 0.5.5
Requires:         R-CRAN-clinUtils >= 0.1.0
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-utils 

%description
Creation of tables of summary statistics or counts for clinical data (for
'TLFs'). These tables can be exported as in-text table (with the
'flextable' package) for a Clinical Study Report (Word format) or a
'topline' presentation (PowerPoint format), or as interactive table (with
the 'DT' package) to an html document for clinical data review.

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
