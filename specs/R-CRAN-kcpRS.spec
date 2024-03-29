%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  kcpRS
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Kernel Change Point Detection on the Running Statistics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-roll 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-RColorBrewer 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-roll 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 

%description
The running statistics of interest is first extracted using a time window
which is slid across the time series, and in each window, the running
statistics value is computed. KCP (Kernel Change Point) detection proposed
by Arlot et al. (2012) <arXiv:1202.3878> is then implemented to flag the
change points on the running statistics (Cabrieto et al., 2018,
<doi:10.1016/j.ins.2018.03.010>). Change points are located by minimizing
a variance criterion based on the pairwise similarities between running
statistics which are computed via the Gaussian kernel. KCP can locate
change points for a given k number of change points. To determine the
optimal k, the KCP permutation test is first carried out by comparing the
variance of the running statistics extracted from the original data to
that of permuted data. If this test is significant, then there is
sufficient evidence for at least one change point in the data. Model
selection is then used to determine the optimal k>0.

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
