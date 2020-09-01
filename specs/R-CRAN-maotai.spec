%global packname  maotai
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Matrix Algebra, Optimization and Inference

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-labdsv 
BuildRequires:    R-CRAN-nabor 
BuildRequires:    R-CRAN-shapes 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-fastcluster 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppDist 
Requires:         R-Matrix 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-Rtsne 
Requires:         R-cluster 
Requires:         R-CRAN-labdsv 
Requires:         R-CRAN-nabor 
Requires:         R-CRAN-shapes 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-fastcluster 
Requires:         R-CRAN-dbscan 

%description
Matrix is an universal and sometimes primary object/unit in applied
mathematics and statistics. We provide a number of algorithms for selected
problems in optimization and statistical inference. For general exposition
to the topic with focus on statistical context, see the book by Banerjee
and Roy (2014, ISBN:9781420095388).

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
