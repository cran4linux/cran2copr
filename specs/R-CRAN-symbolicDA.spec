%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  symbolicDA
%global packver   0.7-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.3
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Symbolic Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-clusterSim 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-shapes 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-RSDA 
Requires:         R-CRAN-clusterSim 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-shapes 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-RSDA 

%description
Symbolic data analysis methods: importing/exporting data from ASSO XML
Files, distance calculation for symbolic data (Ichino-Yaguchi, de Carvalho
measure), zoom star plot, 3d interval plot, multidimensional scaling for
symbolic interval data, dynamic clustering based on distance matrix, HINoV
method for symbolic data, Ichino's feature selection method, principal
component analysis for symbolic interval data, decision trees for symbolic
data based on optimal split with bagging, boosting and random forest
approach (+visualization), kernel discriminant analysis for symbolic data,
Kohonen's self-organizing maps for symbolic data, replication and
profiling, artificial symbolic data generation. (Milligan, G.W., Cooper,
M.C. (1985) <doi:10.1007/BF02294245>, Breiman, L. (1996),
<doi:10.1007/BF00058655>, Hubert, L., Arabie, P. (1985),
<doi:10.1007%%2FBF01908075>, Ichino, M., & Yaguchi, H. (1994),
<doi:10.1109/21.286391>, Rand, W.M. (1971)
<doi:10.1080/01621459.1971.10482356>, Breckenridge, J.N. (2000)
<doi:10.1207/S15327906MBR3502_5>, Groenen, P.J.F, Winsberg, S., Rodriguez,
O., Diday, E. (2006) <doi:10.1016/j.csda.2006.04.003>, Dudek, A. (2007),
<doi:10.1007/978-3-540-70981-7_4>).

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
