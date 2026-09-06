%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qdaR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Read and Analyse Qualitative Coding Exported from Zotero

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-jsonlite 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-MASS 

%description
Reads the versioned exchange files written by the Zotero plugins 'zotQDA'
and 'qdaZ' -- coded fragments, code systems, coding histories and
team-consensus results -- validates them against the shipped contract, and
reproduces the plugin's graphics with 'ggplot2'. Adds what those plugins
deliberately leave out: six agreement coefficients with bootstrap
confidence intervals, the reliability of the segmentation itself,
chi-squared tests of code by group tables with effect sizes,
correspondence analysis, multidimensional scaling and hierarchical
clustering of codes.  Projects from other programs can be read through the
'REFI-QDA' interchange standard <https://www.qdasoftware.org/>, which
makes those analyses available to users of established software that does
not offer them; the subset a '.qdpx' supports is reported on import.
Reference files are included, so every function can be tried without a
Zotero installation.

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
