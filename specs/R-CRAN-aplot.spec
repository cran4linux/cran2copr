%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aplot
%global packver   0.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Decorate a 'ggplot' with Associated Information

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-yulab.utils >= 0.1.9
BuildRequires:    R-CRAN-ggfun >= 0.1.3
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggplotify 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-yulab.utils >= 0.1.9
Requires:         R-CRAN-ggfun >= 0.1.3
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggplotify 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-utils 

%description
For many times, we are not just aligning plots as what 'cowplot' and
'patchwork' did. Users would like to align associated information that
requires axes to be exactly matched in subplots, e.g. hierarchical
clustering with a heatmap. Inspired by the 'Method 2' in 'ggtree' (G Yu
(2018) <doi:10.1093/molbev/msy194>), 'aplot' provides utilities to aligns
associated subplots to a main plot at different sides (left, right, top
and bottom) with axes exactly matched.

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
