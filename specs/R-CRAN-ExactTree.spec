%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ExactTree
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Exact Tree

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-stats 
BuildRequires:    R-grid 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-CRAN-gridtext 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rpart 
Requires:         R-CRAN-partykit 
Requires:         R-CRAN-pracma 
Requires:         R-stats 
Requires:         R-grid 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-formula.tools 
Requires:         R-CRAN-gridtext 
Requires:         R-CRAN-DescTools 
Requires:         R-methods 
Requires:         R-CRAN-rpart 

%description
Grows optimally global trees based on the algorithm defined in "An exact
dynamic programming algorithm for regression and classification trees"
(2011). It is possible to obtain both classification and regression trees
depending on the measurement level of the outcome variable. The algorithm
is based on the dynamic programming principle and guarantees that the
resulting tree is optimal with respect to the chosen impurity measure. The
package also includes a function to visualize the resulting trees, a
function that summarizes the tree with its splitting information and leaf
information, and a predict function that provides estimates for a new
dataset given a model fit.

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
