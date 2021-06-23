%global __brp_check_rpaths %{nil}
%global packname  NetworkReg
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Regression Model on Network-Linked Data with StatisticalInference

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-randnet 
BuildRequires:    R-CRAN-RSpectra 
Requires:         R-Matrix 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-randnet 
Requires:         R-CRAN-RSpectra 

%description
Linear regression model with nonparametric network effects on
network-linked observations. The model is proposed by Le and Li (2020)
<arXiv:2007.00803> and is assumed on observations that are connected by a
network or similar relational data structure. The model does not assume
that the relational data or network structure to be precisely observed;
thus, the method is provably robust to a certain level of perturbation of
the network structure. The package contains the estimation and inference
function for the model.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
