%global __brp_check_rpaths %{nil}
%global packname  mlquantify
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Algorithms for Class Distribution Estimation

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-FNN 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-randomForest 
Requires:         R-stats 
Requires:         R-CRAN-FNN 

%description
Quantification is a prominent machine learning task that has received an
increasing amount of attention in the last years. The objective is to
predict the class distribution of a data sample. This package is a
collection of machine learning algorithms for class distribution
estimation. This package include algorithms from different paradigms of
quantification. These methods are described in the paper: A. Maletzke, W.
Hassan, D. dos Reis, and G. Batista. The importance of the test set size
in quantification assessment. In Proceedings of the Twenty-Ninth
International Joint Conference on Artificial Intelligence, IJCAI20, pages
2640–2646, 2020. <doi:10.24963/ijcai.2020/366>.

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
