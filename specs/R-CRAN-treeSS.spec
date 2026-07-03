%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  treeSS
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Tree-Spatial Scan Statistic for Cluster Detection

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-stats 

%description
Implements the tree-spatial scan statistic for detecting clusters that
combine both spatial and hierarchical structures, as proposed by Cancado
et al. (2025) <doi:10.1007/s10651-025-00670-w>. The method extends
Kulldorff (1997) <doi:10.1080/03610929708831995> circular spatial scan
statistic and the tree-based scan statistic of Kulldorff et al. (2003)
<doi:10.1111/1541-0420.00039> by searching for anomalies in both
geographic regions and branches of hierarchical trees simultaneously. The
package also provides standalone implementations of Kulldorff's circular
spatial scan statistic and the tree-based scan statistic. Statistical
significance is assessed via Monte Carlo simulation under a Poisson or
binomial model, with optional 'OpenMP' parallelization.

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
