%global __brp_check_rpaths %{nil}
%global packname  PINSPlus
%global packver   2.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Clustering Algorithm for Data Integration and Disease Subtyping

License:          LGPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-entropy 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-entropy 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-FNN 
Requires:         R-cluster 
Requires:         R-CRAN-irlba 
Requires:         R-CRAN-mclust 

%description
Provides a robust approach for omics data integration and disease
subtyping. PINSPlus is fast and supports the analysis of large datasets
with hundreds of thousands of samples and features. The software
automatically determines the optimal number of clusters and then
partitions the samples in a way such that the results are robust against
noise and data perturbation (Nguyen et.al. (2019) <DOI:
10.1093/bioinformatics/bty1049>, Nguyen et.al. (2017)<DOI:
10.1101/gr.215129.116>).

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
