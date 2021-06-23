%global __brp_check_rpaths %{nil}
%global packname  GridOnClusters
%global packver   0.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.8
Release:          1%{?dist}%{?buildtag}
Summary:          Cluster-Preserving Multivariate Joint Grid Discretization

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-fossil 
BuildRequires:    R-CRAN-dqrng 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-plotrix 
Requires:         R-CRAN-Rcpp 
Requires:         R-cluster 
Requires:         R-CRAN-fossil 
Requires:         R-CRAN-dqrng 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-plotrix 

%description
Discretize multivariate continuous data using a grid that captures the
joint distribution via preserving clusters in the original data (Wang et
al. 2020). Joint grid discretization is applicable as a data
transformation step to prepare data for model-free inference of
association, function, or causality.

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
