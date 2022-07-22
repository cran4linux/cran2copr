%global __brp_check_rpaths %{nil}
%global packname  briKmeans
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Package for Brik, Fabrik and Fdebrik Algorithms to Initialise Kmeans

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-depthTools 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-splines2 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-depthTools 
Requires:         R-splines 
Requires:         R-CRAN-splines2 
Requires:         R-stats 
Requires:         R-methods 

%description
Implementation of the BRIk, FABRIk and FDEBRIk algorithms to initialise
k-means. These methods are intended for the clustering of multivariate and
functional data, respectively. They make use of the Modified Band Depth
and bootstrap to identify appropriate initial seeds for k-means, which are
proven to be better options than many techniques in the literature.
Torrente and Romo (2021) <doi:10.1007/s00357-020-09372-3> It makes use of
the functions kma and kma.similarity, from the archived package fdakma, by
Alice Parodi et al.

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
