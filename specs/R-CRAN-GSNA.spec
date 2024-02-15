%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GSNA
%global packver   0.1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Gene Set Networking Analysis Package

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-circlize 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-dendextend 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tmod 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-circlize 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-dendextend 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-stringi 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tmod 
Requires:         R-utils 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-Rcpp 

%description
Create networks of gene sets, infer clusters of functionally-related gene
sets based on similarity statistics, and visualize the results. This
package simplifies and accelerates interpretation of pathways analysis
data sets. It is designed to work in tandem with standard pathways
analysis methods, such as the 'GSEA' program (Gene Set Enrichment
Analysis), CERNO (Coincident Extreme Ranks in Numerical Observations,
implemented in the 'tmod' package) and others. Inputs to 'GSNA' are the
outputs of pathways analysis methods: a list of gene sets (or "modules"),
pathways or GO-terms with associated p-values. Since pathways analysis
methods may be used to analyze many different types of data including
transcriptomic, epigenetic, and high-throughput screen data sets, the
'GSNA' pipeline is applicable to these data as well. The use of 'GSNA' has
been described in the following papers: Collins DR, Urbach JM, Racenet ZJ,
Arshad U, Power KA, Newman RM, et al. (2021)
<doi:10.1016/j.immuni.2021.08.007>, Collins DR, Hitschfel J, Urbach JM,
Mylvaganam GH, Ly NL, Arshad U, et al. (2023)
<doi:10.1126/sciimmunol.ade5872>.

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
