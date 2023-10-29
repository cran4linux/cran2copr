%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MSCquartets
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Analyzing Gene Tree Quartets under the Multi-Species Coalescent

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ape >= 5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.10
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-zipfR 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-methods 
Requires:         R-CRAN-ape >= 5.0
Requires:         R-CRAN-Rcpp >= 1.0.10
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-zipfR 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-methods 

%description
Methods for analyzing and using quartets displayed on a collection of gene
trees, primarily to make inferences about the species tree or network
under the multi-species coalescent model. These include quartet hypothesis
tests for the model, as developed by Mitchell et al. (2019)
<doi:10.1214/19-EJS1576>, simplex plots of quartet concordance factors as
presented by Allman et al. (2020) <doi:10.1101/2020.02.13.948083>, species
tree inference methods based on quartet distances of Rhodes (2019)
<doi:10.1109/TCBB.2019.2917204> and Yourdkhani and Rhodes (2019)
<doi:10.1007/s11538-020-00773-4>, and the NANUQ algorithm for inference of
level-1 species networks of Allman et al. (2019)
<doi:10.1186/s13015-019-0159-2>. Software announcement by Rhodes et al.
(2020) <doi:10.1093/bioinformatics/btaa868>.

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
