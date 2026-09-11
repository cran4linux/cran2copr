%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EpiQuestionR
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Questionnaire Analysis for Epidemiology and One Health Research

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Matrix 
Requires:         R-graphics 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-psych 
Requires:         R-stats 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-tibble 

%description
Provides tools for the analysis of questionnaire and survey data in
epidemiological and One Health research. The package supports data
preparation, reliability assessment, exploratory factor analysis,
Kaiser-Meyer-Olkin assessment, parallel analysis, visualization,
reporting, and export of results using a consistent analysis workflow. The
methods are based on established approaches to psychometric and
multivariate analysis; see Kaiser (1974) <doi:10.1007/BF02291575>, Horn
(1965) <doi:10.1007/BF02289447>, and Tabachnick and Fidell (2019,
ISBN:9780134790541).

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
