%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  statGraph
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Methods for Graphs

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-rARPACK 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-rARPACK 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-methods 
Requires:         R-CRAN-mvtnorm 

%description
Contains statistical methods to analyze graphs, such as graph parameter
estimation, model selection based on the Graph Information Criterion,
statistical tests to discriminate two or more populations of graphs,
correlation between graphs, and clustering of graphs. References:
Takahashi et al. (2012) <doi:10.1371/journal.pone.0049949>, Fujita et al.
(2017) <doi:10.3389/fnins.2017.00066>, Fujita et al. (2017)
<doi:10.1016/j.csda.2016.11.016>, Fujita et al. (2019)
<doi:10.1093/comnet/cnz028>.

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
