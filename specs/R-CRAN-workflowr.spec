%global __brp_check_rpaths %{nil}
%global packname  workflowr
%global packver   1.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Framework for Reproducible and Collaborative Data Science

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-callr >= 3.7.0
BuildRequires:    R-CRAN-stringr >= 1.3.0
BuildRequires:    R-CRAN-knitr >= 1.29
BuildRequires:    R-CRAN-fs >= 1.2.7
BuildRequires:    R-CRAN-httpuv >= 1.2.2
BuildRequires:    R-CRAN-rprojroot >= 1.2
BuildRequires:    R-CRAN-rmarkdown >= 1.18
BuildRequires:    R-CRAN-rstudioapi >= 0.6
BuildRequires:    R-CRAN-whisker >= 0.3
BuildRequires:    R-CRAN-git2r >= 0.26.0
BuildRequires:    R-CRAN-getPass 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xfun 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-callr >= 3.7.0
Requires:         R-CRAN-stringr >= 1.3.0
Requires:         R-CRAN-knitr >= 1.29
Requires:         R-CRAN-fs >= 1.2.7
Requires:         R-CRAN-httpuv >= 1.2.2
Requires:         R-CRAN-rprojroot >= 1.2
Requires:         R-CRAN-rmarkdown >= 1.18
Requires:         R-CRAN-rstudioapi >= 0.6
Requires:         R-CRAN-whisker >= 0.3
Requires:         R-CRAN-git2r >= 0.26.0
Requires:         R-CRAN-getPass 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-httr 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-xfun 
Requires:         R-CRAN-yaml 

%description
Provides a workflow for your analysis projects by combining literate
programming ('knitr' and 'rmarkdown') and version control ('Git', via
'git2r') to generate a website containing time-stamped, versioned, and
documented results.

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
