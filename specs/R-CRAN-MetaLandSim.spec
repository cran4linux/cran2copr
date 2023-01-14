%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MetaLandSim
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Landscape and Range Expansion Simulation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-googleVis 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-spatstat.random 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-zipfR 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-e1071 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-googleVis 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat.random 
Requires:         R-stats 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-zipfR 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-knitr 

%description
Tools to generate random landscape graphs, evaluate species occurrence in
dynamic landscapes, simulate future landscape occupation and evaluate
range expansion when new empty patches are available (e.g. as a result of
climate change). References: Mestre, F., Canovas, F., Pita, R., Mira, A.,
Beja, P. (2016) <doi:10.1016/j.envsoft.2016.03.007>; Mestre, F., Risk, B.,
Mira, A., Beja, P., Pita, R. (2017) <doi:10.1016/j.ecolmodel.2017.06.013>;
Mestre, F., Pita, R., Mira, A., Beja, P. (2020)
<doi:10.1186/s12898-019-0273-5>.

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
