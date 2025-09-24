%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tcv
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Determining the Number of Factors in Poisson Factor Models via Thinning Cross-Validation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-GFM 
BuildRequires:    R-CRAN-countsplit 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-stats 
Requires:         R-CRAN-GFM 
Requires:         R-CRAN-countsplit 
Requires:         R-CRAN-irlba 

%description
Implements methods for selecting the number of factors in Poisson factor
models, with a primary focus on Thinning Cross-Validation (TCV). The TCV
method is based on the 'data thinning' technique, which probabilistically
partitions each count observation into training and test sets while
preserving the underlying factor structure. The Poisson factor model is
then fit on the training set, and model selection is performed by
comparing predictive performance on the test set. This toolkit is designed
for researchers working with high-dimensional count data in fields such as
genomics, text mining, and social sciences. The data thinning methodology
is detailed in Dharamshi et al. (2025) <doi:10.1080/01621459.2024.2353948>
and Wang et al. (2025) <doi:10.1080/01621459.2025.2546577>.

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
