%global packname  eat
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Efficiency Analysis Trees

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-conflicted 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggparty 
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-lpSolveAPI 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-conflicted 
Requires:         R-stats 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggparty 
Requires:         R-CRAN-partykit 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-lpSolveAPI 
Requires:         R-utils 
Requires:         R-CRAN-reshape2 

%description
Functions are provided to determine production frontiers and technical
efficiency measures through non-parametric techniques based upon
regression trees. The package includes code for estimating radial input,
output, directional and additive measures, plotting graphical
representations of the scores and the production frontiers by means of
trees, and determining rankings of importance of input variables in the
analysis. Additionally, an adaptation of Random Forest by a set of
individual Efficiency Analysis Trees for estimating technical efficiency
is also included. More details in: <doi:10.1016/j.eswa.2020.113783>.

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
