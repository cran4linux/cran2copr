%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ccar3
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Canonical Correlation Analysis via Reduced Rank Regression

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-caret 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-caret 

%description
Canonical correlation analysis (CCA) via reduced-rank regression with
support for regularization and cross-validation. Several methods for
estimating CCA in high-dimensional settings are implemented. The first set
of methods, cca_rrr() (and variants: cca_group_rrr() and cca_graph_rrr()),
assumes that one dataset is high-dimensional and the other is
low-dimensional, while the second, ecca() (for Efficient CCA) assumes that
both datasets are high-dimensional. For both methods, standard l1
regularization as well as group-lasso regularization are available.
cca_graph_rrr further supports total variation regularization when there
is a known graph structure among the variables of the high-dimensional
dataset. In this case, the loadings of the canonical directions of the
high-dimensional dataset are assumed to be smooth on the graph. For more
details see Donnat and Tuzhilina (2024) <doi:10.48550/arXiv.2405.19539>
and Wu, Tuzhilina and Donnat (2025) <doi:10.48550/arXiv.2507.11160>.

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
