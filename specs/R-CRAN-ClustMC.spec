%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ClustMC
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Cluster-Based Multiple Comparisons

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-procs 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-usedist 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dplyr 
Requires:         R-graphics 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-procs 
Requires:         R-CRAN-psych 
Requires:         R-stats 
Requires:         R-CRAN-usedist 

%description
Multiple comparison techniques are typically applied following an F test
from an ANOVA to decide which means are significantly different from one
another. As an alternative to traditional methods, cluster analysis can be
performed to group the means of different treatments into non-overlapping
clusters. Treatments in different groups are considered statistically
different. Several approaches have been proposed, with varying clustering
methods and cut-off criteria. This package implements cluster-based
multiple comparisons tests and also provides a visual representation in
the form of a dendrogram. Di Rienzo, J. A., Guzman, A. W., & Casanoves, F.
(2002) <jstor.org/stable/1400690>. Bautista, M. G., Smith, D. W., &
Steiner, R. L. (1997) <doi:10.2307/1400402>.

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
