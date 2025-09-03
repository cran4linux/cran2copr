%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cmAnalysis
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Process and Visualise Concept Mapping Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-factoextra 
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-pheatmap 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-factoextra 
Requires:         R-CRAN-clue 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-pheatmap 

%description
Concept maps are versatile tools used across disciplines to enhance
understanding, teaching, brainstorming, and information organization. This
package provides functions for processing and visualizing concept mapping
data, involving the sequential use of cluster analysis (for sorting
participants and statements), multidimensional scaling (for positioning
statements in a conceptual space), and visualization techniques, including
point cluster maps and dendrograms. The methodology and its validity are
discussed in Kampen, J.K., Hageman, J.A., Breuer, M., & Tobi, H. (2025).
"The validity of concept mapping: let's call a spade a spade." Qual Quant.
<doi:10.1007/s11135-025-02351-z>.

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
