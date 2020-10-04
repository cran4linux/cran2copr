%global packname  fDMA
%global packver   2.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic Model Averaging and Dynamic Model Selection forContinuous Outcomes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-itertools 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-gplots 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-itertools 
Requires:         R-parallel 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-png 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-CRAN-tseries 
Requires:         R-utils 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 

%description
Allows to estimate dynamic model averaging, dynamic model selection and
median probability model. The original methods are implemented, as well
as, selected further modifications of these methods. In particular the
user might choose between recursive moment estimation and exponentially
moving average for variance updating. Inclusion probabilities might be
modified in a way using 'Google Trends'. The code is written in a way
which minimises the computational burden (which is quite an obstacle for
dynamic model averaging if many variables are used). For example, this
package allows for parallel computations and Occam's window approach. The
package is designed in a way that is hoped to be especially useful in
economics and finance. Main reference: Raftery, A.E., Karny, M., Ettler,
P. (2010) <doi:10.1198/TECH.2009.08104>.

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
