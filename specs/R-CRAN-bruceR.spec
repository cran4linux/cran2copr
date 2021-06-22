%global packname  bruceR
%global packver   0.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.2
Release:          1%{?dist}%{?buildtag}
Summary:          Broadly Useful Convenient and Efficient R Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pacman 
BuildRequires:    R-CRAN-jmv 
BuildRequires:    R-CRAN-performance 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-see 
Requires:         R-CRAN-pacman 
Requires:         R-CRAN-jmv 
Requires:         R-CRAN-performance 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggtext 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-see 

%description
Broadly useful convenient and efficient R functions that bring users
concise and elegant R data analyses. This package includes easy-to-use
functions for (1) basic R programming (e.g., set working directory to
where the current file is, print strings with rich formats and colors);
(2) multivariate computation (e.g., compute scale sums/means/... with
reverse scoring); (3) reliability and factor analyses; (4) descriptive
statistics and correlation analyses; (5) multi-factor analysis of variance
(ANOVA), simple-effect analysis, and post-hoc multiple comparison; (6)
tidy report of regression models and other results (to R Console and MS
Word); (7) mediation and moderation analyses (PROCESS); and (8) additional
toolbox for statistics and graphics.

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
