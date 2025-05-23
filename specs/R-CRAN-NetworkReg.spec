%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NetworkReg
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Linear Regression Models on Network-Linked Data with Statistical Inference

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-randnet 
BuildRequires:    R-CRAN-RSpectra 
Requires:         R-stats 
Requires:         R-CRAN-randnet 
Requires:         R-CRAN-RSpectra 

%description
Linear regression model and generalized linear models with nonparametric
network effects on network-linked observations. The model is originally
proposed by Le and Li (2022) <doi:10.48550/arXiv.2007.00803> and is
assumed on observations that are connected by a network or similar
relational data structure. A more recent work by Wang, Le and Li (2024)
<doi:10.48550/arXiv.2410.01163> further extends the framework to
generalized linear models. All these models are implemented in the current
package. The model does not assume that the relational data or network
structure to be precisely observed; thus, the method is provably robust to
a certain level of perturbation of the network structure. The package
contains the estimation and inference function for the model.

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
