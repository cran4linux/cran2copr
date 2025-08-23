%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fusedTree
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fused Partitioned Regression for Clinical and Omics Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-splitTools 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-treeClust 
BuildRequires:    R-CRAN-partykit 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-splitTools 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-treeClust 
Requires:         R-CRAN-partykit 

%description
Fit (generalized) linear regression models in each leaf node of a tree.
The tree is constructed using clinical variables only. The linear
regression models are constructed using (high-dimensional) omics variables
only. The leaf-node-specific regression models are estimated using the
penalized likelihood including a standard ridge (L2) penalty and a fusion
penalty that links the leaf-node-specific regression models to one
another. The intercepts of the leaf nodes reflect the effects of the
clinical variables and are left unpenalized. The tree, fitted with the
clinical variables only, should be constructed outside of the package with
the 'rpart' 'R' package. See Goedhart and others (2024)
<doi:10.48550/arXiv.2411.02396> for details on the method.

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
