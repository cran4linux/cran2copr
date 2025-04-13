%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ReMFPCA
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Regularized Multivariate Functional Principal Component Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-Matrix 

%description
Methods and tools for implementing regularized multivariate functional
principal component analysis ('ReMFPCA') for multivariate functional data
whose variables might be observed over different dimensional domains.
'ReMFPCA' is an object-oriented interface leveraging the extensibility and
scalability of R6. It employs a parameter vector to control the smoothness
of each functional variable. By incorporating smoothness constraints as
penalty terms within a regularized optimization framework, 'ReMFPCA'
generates smooth multivariate functional principal components, offering a
concise and interpretable representation of the data. For detailed
information on the methods and techniques used in 'ReMFPCA', please refer
to Haghbin et al. (2023) <doi:10.48550/arXiv.2306.13980>.

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
