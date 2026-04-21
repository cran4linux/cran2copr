%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  confMeta
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Confidence Curves and P-Value Functions for Meta-Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-meta 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-ReplicationSuccess 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-meta 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-ReplicationSuccess 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-rlang 

%description
Provides tools for the combination of individual study results in
meta-analyses using 'p-value' functions. Implements various combination
methods including those by Fisher, Stouffer, Tippett, Edgington along with
weighted generalizations. Contains functionality for the visualization and
calculation of confidence curves and drapery plots to summarize evidence
across studies.

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
