%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ANOPA
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Analyses of Proportions using Anscombe Transform

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-scales >= 1.2.1
BuildRequires:    R-CRAN-superb >= 0.95.0
BuildRequires:    R-CRAN-Rdpack >= 0.7
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rrapply 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-scales >= 1.2.1
Requires:         R-CRAN-superb >= 0.95.0
Requires:         R-CRAN-Rdpack >= 0.7
Requires:         R-stats 
Requires:         R-CRAN-rrapply 
Requires:         R-utils 

%description
Analyses of Proportions can be performed on the Anscombe (arcsine-related)
transformed data. The 'ANOPA' package can analyze proportions obtained
from up to four factors. The factors can be within-subject or
between-subject or a mix of within- and between-subject. The main, omnibus
analysis can be followed by additive decompositions into interaction
effects, main effects, simple effects, contrast effects, etc., mimicking
precisely the logic of ANOVA. For that reason, we call this set of tools
'ANOPA' (Analysis of Proportion using Anscombe transform) to highlight its
similarities with ANOVA. The 'ANOPA' framework also allows plots of
proportions easy to obtain along with confidence intervals. Finally,
effect sizes and planning statistical power are easily done under this
framework. Only particularity, the 'ANOPA' computes F statistics which
have an infinite degree of freedom on the denominator. See Laurencelle and
Cousineau (2023) <doi:10.3389/fpsyg.2022.1045436>.

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
