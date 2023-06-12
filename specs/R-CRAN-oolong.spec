%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  oolong
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Create Validation Tests for Automated Content Analysis

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-quanteda >= 3.0.0
BuildRequires:    R-CRAN-keyATM >= 0.2.2
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-irr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-quanteda >= 3.0.0
Requires:         R-CRAN-keyATM >= 0.2.2
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-irr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-cli 
Requires:         R-stats 
Requires:         R-utils 

%description
Intended to create standard human-in-the-loop validity tests for typical
automated content analysis such as topic modeling and dictionary-based
methods. This package offers a standard workflow with functions to
prepare, administer and evaluate a human-in-the-loop validity test. This
package provides functions for validating topic models using word
intrusion, topic intrusion (Chang et al. 2009,
<https://papers.nips.cc/paper/3700-reading-tea-leaves-how-humans-interpret-topic-models>)
and word set intrusion (Ying et al. 2021) <doi:10.1017/pan.2021.33> tests.
This package also provides functions for generating gold-standard data
which are useful for validating dictionary-based methods. The default
settings of all generated tests match those suggested in Chang et al.
(2009) and Song et al. (2020) <doi:10.1080/10584609.2020.1723752>.

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
