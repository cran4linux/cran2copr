%global packname  GeneralizedUmatrix
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Credible Visualization for Two-Dimensional Projections of Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-ggplot2 

%description
Projections are common dimensionality reduction methods, which represent
high-dimensional data in a two-dimensional space. However, when
restricting the output space to two dimensions, which results in a two
dimensional scatter plot (projection) of the data, low dimensional
similarities do not represent high dimensional distances coercively
[Thrun, 2018]. This could lead to a misleading interpretation of the
underlying structures [Thrun, 2018]. By means of the 3D topographic map
the generalized Umatrix is able to depict errors of these two-dimensional
scatter plots. The package is based on the book of Thrun, M.C.:
"Projection Based Clustering through Self-Organization and Swarm
Intelligence" (2018) <DOI:10.1007/978-3-658-20540-9>.

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
