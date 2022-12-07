%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DBERlibR
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Assessment Data Analysis for Discipline-Based Education Research

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-rstatix 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-car 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-rstatix 
Requires:         R-CRAN-tibble 

%description
Discipline-Based Education Research scientists repeatedly analyze
assessment data to ensure question items’ reliability and examine the
efficacy of a new educational intervention. Analyzing assessment data
comprises multiple steps and statistical techniques that consume much of
researchers’ time and are error-prone. While education research continues
to grow across many disciplines of science, technology, engineering, and
mathematics (STEM), the discipline-based education research community
lacks tools to streamline education research data analysis. ‘DBERlibR’—an
‘R’ package to streamline and automate assessment data processing and
analysis—fills this gap. The package reads user-provided assessment data,
cleans them, merges multiple datasets (as necessary), checks assumption(s)
for specific statistical techniques (as necessary), applies various
statistical tests (e.g., one-way analysis of covariance, one-way
repeated-measures analysis of variance), and presents and interprets the
results all at once. By providing the most frequently used analytic
techniques, this package will contribute to education research by
facilitating the creation and widespread use of evidence-based knowledge
and practices. The outputs contain a sample interpretation of the results
for users’ convenience. User inputs are minimal; they only need to prepare
the data files as instructed and type a function in the 'R' console to
conduct a specific data analysis.n For descriptions of the statistical
methods employed in package, refer to the following Encyclopedia of
Research Design, edited by Salkind, N. (2010) <doi:10.4135/9781412961288>.

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
