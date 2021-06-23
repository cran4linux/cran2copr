%global __brp_check_rpaths %{nil}
%global packname  bigSurvSGD
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Big Survival Analysis Using Stochastic Gradient Descent

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.4
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-survival 
Requires:         R-CRAN-Rcpp >= 1.0.4
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-bigmemory 
Requires:         R-CRAN-doParallel 
Requires:         R-survival 

%description
Fits Cox model via stochastic gradient descent. This implementation avoids
computational instability of the standard Cox Model when dealing large
datasets. Furthermore, it scales up with large datasets that do not fit
the memory. It also handles large sparse datasets using proximal
stochastic gradient descent algorithm. For more details about the method,
please see Aliasghar Tarkhan and Noah Simon (2020) <arXiv:2003.00116v2>.

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
