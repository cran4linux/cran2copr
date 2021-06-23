%global __brp_check_rpaths %{nil}
%global packname  statgenSTA
%global packver   1.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          1%{?dist}%{?buildtag}
Summary:          Single Trial Analysis (STA) of Field Trials

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-scales >= 1.1.0
BuildRequires:    R-CRAN-SpATS >= 1.0.10
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-mapproj 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-qtl 
BuildRequires:    R-CRAN-xtable 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-scales >= 1.1.0
Requires:         R-CRAN-SpATS >= 1.0.10
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-mapproj 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-qtl 
Requires:         R-CRAN-xtable 

%description
Phenotypic analysis of field trials using mixed models with and without
spatial components. One of a series of statistical genetic packages for
streamlining the analysis of typical plant breeding experiments developed
by Biometris. Some functions have been created to be used in conjunction
with the R package 'asreml' for the 'ASReml' software, which can be
obtained upon purchase from 'VSN' international
(<https://www.vsni.co.uk/software/asreml-r>).

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
