%global __brp_check_rpaths %{nil}
%global packname  scINSIGHT
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Interpretation of Heterogeneous Single-Cell Gene Expression Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-igraph 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-stringr 

%description
We develop a novel matrix factorization tool named 'scINSIGHT' to jointly
analyze multiple single-cell gene expression samples from biologically
heterogeneous sources, such as different disease phases, treatment groups,
or developmental stages. Given multiple gene expression samples from
different biological conditions, 'scINSIGHT' simultaneously identifies
common and condition-specific gene modules and quantify their expression
levels in each sample in a lower-dimensional space. With the factorized
results, the inferred expression levels and memberships of common gene
modules can be used to cluster cells and detect cell identities, and the
condition-specific gene modules can help compare functional differences in
transcriptomes from distinct conditions. Please also see Qian K, Fu SW, Li
HW, Li WV (2022) <doi:10.1186/s13059-022-02649-3>.

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
