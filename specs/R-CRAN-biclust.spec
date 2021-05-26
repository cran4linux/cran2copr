%global packname  biclust
%global packver   2.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          BiCluster Algorithms

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-flexclust 
BuildRequires:    R-CRAN-additivityTests 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-MASS 
Requires:         R-grid 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-lattice 
Requires:         R-methods 
Requires:         R-CRAN-flexclust 
Requires:         R-CRAN-additivityTests 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 

%description
The main function biclust() provides several algorithms to find biclusters
in two-dimensional data: Cheng and Church (2000, ISBN:1-57735-115-0),
spectral (2003) <doi:10.1101/gr.648603>, plaid model (2005)
<doi:10.1016/j.csda.2004.02.003>, xmotifs (2003)
<doi:10.1142/9789812776303_0008> and bimax (2006)
<doi:10.1093/bioinformatics/btl060>. In addition, the package provides
methods for data preprocessing (normalization and discretisation),
visualisation, and validation of bicluster solutions.

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
