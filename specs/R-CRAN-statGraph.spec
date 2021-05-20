%global packname  statGraph
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Methods for Graphs

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
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
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-rARPACK 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 

%description
Contains statistical methods to analyze graphs, such as graph parameter
estimation, model selection based on the GIC (Graph Information
Criterion), statistical tests to discriminate two or more populations of
graphs (ANOGVA - Analysis of Graph Variability), correlation between
graphs, and clustering of graphs. References: Takahashi et al. (2012)
<doi:10.1371/journal.pone.0049949>, Futija et al. (2017)
<doi:10.3389/fnins.2017.00066>, Fujita et al. (2017)
<doi:10.1016/j.csda.2016.11.016>, Tang et al. (2017)
<doi:10.3150/15-BEJ789>, Tang et al. (2017)
<doi:10.1080/10618600.2016.1193505>, Ghoshdastidar et al. (2017)
<arXiv:1705.06168>, Ghoshdastidar et al. (2017) <arXiv:1707.00833>,
Cerqueira et al. (2017) <doi:10.1109/TNSE.2017.2674026>, Fraiman and
Fraiman (2018) <doi:10.1038/s41598-018-23152-5>, Fujita et al. (2019)
<doi:10.1093/comnet/cnz028>.

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
