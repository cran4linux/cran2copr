%global packname  altmeta
%global packver   3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Alternative Meta-Analysis Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags >= 4.6
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-rjags >= 4.6
Requires:         R-CRAN-coda 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-metafor 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides alternative statistical methods for meta-analysis, including: -
bivariate generalized linear mixed models for synthesizing odds ratios,
relative risks, and risk differences (Chu et al., 2012
<doi:10.1177/0962280210393712>) - heterogeneity tests and measures that
are robust to outliers (Lin et al., 2017 <doi:10.1111/biom.12543>); -
measures, tests, and visualization tools for publication bias or
small-study effects (Lin and Chu, 2018 <doi:10.1111/biom.12817>; Lin, 2019
<doi:10.1002/jrsm.1340>; Lin, 2020 <doi:10.1177/0962280220910172>; Shi et
al., 2020 <doi:10.1002/jrsm.1415>); - meta-analysis of diagnostic tests
for synthesizing sensitivities, specificities, etc. (Reitsma et al., 2005
<doi:10.1016/j.jclinepi.2005.02.022>; Chu and Cole, 2006
<doi:10.1016/j.jclinepi.2006.06.011>); - meta-analysis methods for
synthesizing proportions (Lin and Chu, 2020
<doi:10.1097/ede.0000000000001232>); - models for multivariate
meta-analysis (Lin and Chu, 2018 <doi:10.1002/jrsm.1293>).

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
