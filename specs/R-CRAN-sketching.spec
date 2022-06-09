%global __brp_check_rpaths %{nil}
%global packname  sketching
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Sketching of Data via Random Subspace Embeddings

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-phangorn >= 2.8.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-phangorn >= 2.8.1
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-stats 
Requires:         R-CRAN-MASS 

%description
Construct sketches of data via random subspace embeddings. For more
details, see the following papers. Lee, S. and Ng, S. (2022). "Least
Squares Estimation Using Sketched Data with Heteroskedastic Errors,"
<arXiv:2007.07781>, accepted for presentation at the Thirty-ninth
International Conference on Machine Learning (ICML 2022). Lee, S. and Ng,
S. (2020). "An Econometric Perspective on Algorithmic Subsampling," Annual
Review of Economics, 12(1): 45–80.

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
