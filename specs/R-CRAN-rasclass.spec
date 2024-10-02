%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rasclass
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Supervised Raster Image Classification

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-RSNNS 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-randomForest 
Requires:         R-methods 
Requires:         R-CRAN-car 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-RSNNS 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-randomForest 

%description
Software to perform supervised and pixel based raster image
classification. It has been designed to facilitate land-cover analysis.
Five classification algorithms can be used: Maximum Likelihood
Classification, Multinomial Logistic Regression, Neural Networks, Random
Forests and Support Vector Machines. The output includes the classified
raster and standard classification accuracy assessment such as the
accuracy matrix, the overall accuracy and the kappa coefficient. An option
for in-sample verification is available.

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
