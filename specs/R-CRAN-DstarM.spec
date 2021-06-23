%global __brp_check_rpaths %{nil}
%global packname  DstarM
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analyze Two Choice Reaction Time Data with the D*M Method

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-DEoptim 
BuildRequires:    R-CRAN-RWiener 
BuildRequires:    R-CRAN-rtdists 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-DEoptim 
Requires:         R-CRAN-RWiener 
Requires:         R-CRAN-rtdists 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Rcpp 

%description
A collection of functions to estimate parameters of a diffusion model via
a D*M analysis. Build in models are: the Ratcliff diffusion model, the
RWiener diffusion model, and Linear Ballistic Accumulator models. Custom
models functions can be specified as long as they have a density function.

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
