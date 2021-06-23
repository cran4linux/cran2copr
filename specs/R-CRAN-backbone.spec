%global __brp_check_rpaths %{nil}
%global packname  backbone
%global packver   1.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Extracts the Backbone from Weighted Graphs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-PoissonBinomial 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-network 
Requires:         R-CRAN-PoissonBinomial 

%description
Provides methods for extracting from a weighted graph a binary or signed
backbone that retains only the significant edges. The user may input a
weighted graph, or a bipartite graph from which a weighted graph is first
constructed via projection. Backbone extraction methods include the
stochastic degree sequence model (SDSM; Neal, Z. P. (2014).
<doi:10.1016/j.socnet.2014.06.001>), the fixed degree sequence model
(FDSM; Zweig, K. A., and Kaufmann, M. (2011).
<doi:10.1007/s13278-011-0021-0>), the fixed row model (FRM; Neal, Z. P.
(2013). <doi:10.1007/s13278-013-0107-y>), the fixed column model (FCM;
Neal, Domagalski, and Sagan (2021). <arXiv:2105.13396>), the fixed fill
model (FFM; Neal, Domagalski, and Sagan (2021). <arXiv:2105.13396>), and a
universal threshold method.

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
