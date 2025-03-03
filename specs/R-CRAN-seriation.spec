%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  seriation
%global packver   1.5.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.7
Release:          1%{?dist}%{?buildtag}
Summary:          Infrastructure for Ordering Objects Using Seriation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-CRAN-ca 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-gclus 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-qap 
BuildRequires:    R-CRAN-registry 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-TSP 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-ca 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-gclus 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-qap 
Requires:         R-CRAN-registry 
Requires:         R-stats 
Requires:         R-CRAN-TSP 
Requires:         R-CRAN-vegan 

%description
Infrastructure for ordering objects with an implementation of several
seriation/sequencing/ordination techniques to reorder matrices,
dissimilarity matrices, and dendrograms. Also provides (optimally)
reordered heatmaps, color images and clustering visualizations like
dissimilarity plots, and visual assessment of cluster tendency plots (VAT
and iVAT). Hahsler et al (2008) <doi:10.18637/jss.v025.i03>.

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
