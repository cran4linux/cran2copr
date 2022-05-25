%global __brp_check_rpaths %{nil}
%global packname  clusterSim
%global packver   0.50-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.50.1
Release:          1%{?dist}%{?buildtag}
Summary:          Searching for Optimal Clustering Procedure for a Data Set

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-R2HTML 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-R2HTML 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Distance measures (GDM1, GDM2, Sokal-Michener, Bray-Curtis, for symbolic
interval-valued data), cluster quality indices (Calinski-Harabasz,
Baker-Hubert, Hubert-Levine, Silhouette, Krzanowski-Lai, Hartigan, Gap,
Davies-Bouldin), data normalization formulas (metric data, interval-valued
symbolic data), data generation (typical and non-typical data), HINoV
method, replication analysis, linear ordering methods, spectral
clustering, agreement indices between two partitions, plot functions (for
categorical and symbolic interval-valued data). (MILLIGAN, G.W., COOPER,
M.C. (1985) <doi:10.1007/BF02294245>, HUBERT, L., ARABIE, P. (1985)
<doi:10.1007%%2FBF01908075>, RAND, W.M. (1971)
<doi:10.1080/01621459.1971.10482356>, JAJUGA, K., WALESIAK, M. (2000)
<doi:10.1007/978-3-642-57280-7_11>, MILLIGAN, G.W., COOPER, M.C. (1988)
<doi:10.1007/BF01897163>, JAJUGA, K., WALESIAK, M., BAK, A. (2003)
<doi:10.1007/978-3-642-55721-7_12>, DAVIES, D.L., BOULDIN, D.W. (1979)
<doi:10.1109/TPAMI.1979.4766909>, CALINSKI, T., HARABASZ, J. (1974)
<doi:10.1080/03610927408827101>, HUBERT, L. (1974)
<doi:10.1080/01621459.1974.10480191>, TIBSHIRANI, R., WALTHER, G., HASTIE,
T. (2001) <doi:10.1111/1467-9868.00293>, BRECKENRIDGE, J.N. (2000)
<doi:10.1207/S15327906MBR3502_5>, WALESIAK, M., DUDEK, A. (2008)
<doi:10.1007/978-3-540-78246-9_11>).

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
