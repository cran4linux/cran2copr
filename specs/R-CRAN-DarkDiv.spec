%global __brp_check_rpaths %{nil}
%global packname  DarkDiv
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating Dark Diversity and Site-Specific Species Pools

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-stats 
Requires:         R-CRAN-vegan 
Requires:         R-stats 

%description
Estimation of dark diversity and site-specific species pools using species
co-occurrences. It includes implementations of probabilistic dark
diversity based on the Hypergeometric distribution, as well as estimations
based on the Beals index, which can be transformed to binary predictions
using different thresholds, or transformed into a favorability index. All
methods include the possibility of using a calibration dataset that is
used to estimate the indication matrix between pairs of species, or to
estimate dark diversity directly on a single dataset. See De Caceres and
Legendre (2008) <doi:10.1007/s00442-008-1017-y>, Lewis et al. (2016)
<doi:10.1111/2041-210X.12443>, Partel et al. (2011)
<doi:10.1016/j.tree.2010.12.004>, Real et al. (2017)
<doi:10.1093/sysbio/syw072> for further information.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
