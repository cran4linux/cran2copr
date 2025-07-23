%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  r4lineups
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Inference on Lineup Fairness

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-here 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-here 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-utils 

%description
Since the early 1970s eyewitness testimony researchers have recognised the
importance of estimating properties such as lineup bias (is the lineup
biased against the suspect, leading to a rate of choosing higher than one
would expect by chance?), and lineup size (how many reasonable choices are
in fact available to the witness? A lineup is supposed to consist of a
suspect and a number of additional members, or foils, whom a poor-quality
witness might mistake for the perpetrator). Lineup measures are
descriptive, in the first instance, but since the earliest articles in the
literature researchers have recognised the importance of reasoning
inferentially about them. This package contains functions to compute
various properties of laboratory or police lineups, and is intended for
use by researchers in forensic psychology and/or eyewitness testimony
research. Among others, the r4lineups package includes functions for
calculating lineup proportion, functional size, various estimates of
effective size, diagnosticity ratio, homogeneity of the diagnosticity
ratio, ROC curves for confidence x accuracy data and the degree of
similarity of faces in a lineup.

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
