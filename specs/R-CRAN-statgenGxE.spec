%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  statgenGxE
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Genotype by Environment (GxE) Analysis

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Recommends:       /usr/bin/pdflatex
BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-statgenSTA >= 1.0.6
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-xtable 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-statgenSTA >= 1.0.6
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-lme4 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-xtable 

%description
Analysis of multi environment data of plant breeding experiments following
the analyses described in Malosetti, Ribaut, and van Eeuwijk (2013),
<doi:10.3389/fphys.2013.00044>. One of a series of statistical genetic
packages for streamlining the analysis of typical plant breeding
experiments developed by Biometris. Some functions have been created to be
used in conjunction with the R package 'asreml' for the 'ASReml' software,
which can be obtained upon purchase from 'VSN' international
(<https://vsni.co.uk/software/asreml-r>).

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
