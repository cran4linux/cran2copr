%global __brp_check_rpaths %{nil}
%global packname  bruceR
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          1%{?dist}%{?buildtag}
Summary:          Broadly Useful Convenient and Efficient R Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-effectsize 
BuildRequires:    R-CRAN-performance 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-see 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-effectsize 
Requires:         R-CRAN-performance 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggtext 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-see 

%description
Broadly useful convenient and efficient R functions that bring users
concise and elegant R data analyses. This package includes easy-to-use
functions for (1) basic R programming (e.g., set working directory to the
path of currently opened file, import/export data from/to files with any
format, print strings with rich formats and colors); (2) multivariate
computation (e.g., compute scale sums/means/... with reverse scoring); (3)
reliability analyses and factor analyses; (4) descriptive statistics and
correlation analyses; (5) t-test, multi-factor analysis of variance
(ANOVA), simple-effect analysis, and post-hoc multiple comparison; (6)
tidy report of statistical models (to R Console and Microsoft Word); (7)
mediation and moderation analyses (PROCESS); and (8) additional toolbox
for statistics and graphics.

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
