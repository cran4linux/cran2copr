%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  writeAlizer
%global packver   1.7.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.3
Release:          1%{?dist}%{?buildtag}
Summary:          Generate Predicted Writing Quality Scores

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-caret 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-magrittr 
Requires:         R-stats 
Requires:         R-CRAN-tidyselect 

%description
Imports variables from 'ReaderBench' (Dascalu et al.,
2018)<doi:10.1007/978-3-319-66610-5_48>, 'Coh-Metrix' (McNamara et al.,
2014)<doi:10.1017/CBO9780511894664>, and/or 'GAMET' (Crossley et al.,
2019) <doi:10.17239/jowr-2019.11.02.01> output files; downloads predictive
scoring models described in Mercer & Cannon
(2022)<doi:10.31244/jero.2022.01.03> and Mercer et
al.(2021)<doi:10.1177/0829573520987753>; and generates predicted writing
quality and curriculum-based measurement (McMaster & Espin,
2007)<doi:10.1177/00224669070410020301> scores.

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
