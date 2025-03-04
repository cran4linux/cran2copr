%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SpaTopic
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Topic Inference to Identify Tissue Architecture in Multiplexed Images

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-methods >= 3.4
BuildRequires:    R-CRAN-RANN >= 2.6.0
BuildRequires:    R-CRAN-foreach >= 1.5.0
BuildRequires:    R-CRAN-sf >= 1.0.12
BuildRequires:    R-CRAN-iterators >= 1.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-methods >= 3.4
Requires:         R-CRAN-RANN >= 2.6.0
Requires:         R-CRAN-foreach >= 1.5.0
Requires:         R-CRAN-sf >= 1.0.12
Requires:         R-CRAN-iterators >= 1.0
Requires:         R-CRAN-Rcpp >= 0.12.0

%description
A novel spatial topic model to integrate both cell type and spatial
information to identify the complex spatial tissue architecture on
multiplexed tissue images without human intervention. The Package
implements a collapsed Gibbs sampling algorithm for inference. 'SpaTopic'
is scalable to large-scale image datasets without extracting neighborhood
information for every single cell. For more details on the methodology,
see <https://xiyupeng.github.io/SpaTopic/>.

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
