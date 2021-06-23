%global __brp_check_rpaths %{nil}
%global packname  simPop
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Simulation of Complex Synthetic Data Information

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-vcd 
BuildRequires:    R-CRAN-laeken 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-VIM 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-party 
BuildRequires:    R-CRAN-EnvStats 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-wrswoR 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-vcd 
Requires:         R-CRAN-laeken 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-RcppArmadillo 
Requires:         R-CRAN-e1071 
Requires:         R-parallel 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-VIM 
Requires:         R-methods 
Requires:         R-CRAN-party 
Requires:         R-CRAN-EnvStats 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-wrswoR 
Requires:         R-CRAN-data.table 

%description
Tools and methods to simulate populations for surveys based on auxiliary
data. The tools include model-based methods, calibration and combinatorial
optimization algorithms, see Templ, Kowarik and Meindl (2017)
<doi:10.18637/jss.v079.i10>) and Templ (2017)
<doi:10.1007/978-3-319-50272-4>. The package was developed with support of
the International Household Survey Network, DFID Trust Fund TF011722 and
funds from the World bank.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
