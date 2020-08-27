%global packname  TreeLS
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Terrestrial Point Cloud Processing of Forest Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-lidR >= 3.0.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-data.table >= 1.12.0
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-CRAN-dismo 
BuildRequires:    R-CRAN-nabor 
BuildRequires:    R-CRAN-benchmarkme 
BuildRequires:    R-CRAN-rlas 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-mathjaxr 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-lidR >= 3.0.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-data.table >= 1.12.0
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-deldir 
Requires:         R-CRAN-dismo 
Requires:         R-CRAN-nabor 
Requires:         R-CRAN-benchmarkme 
Requires:         R-CRAN-rlas 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-mathjaxr 

%description
High performance algorithms for manipulation of terrestrial 'LiDAR' (but
not only) point clouds for use in research and forest monitoring
applications, being fully compatible with the 'LAS' infrastructure of
'lidR'. For in depth descriptions of stem denoising and segmentation
algorithms refer to Conto et al. (2017)
<doi:10.1016/j.compag.2017.10.019>.

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
