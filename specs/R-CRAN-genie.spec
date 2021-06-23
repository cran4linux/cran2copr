%global __brp_check_rpaths %{nil}
%global packname  genie
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Fast, Robust, and Outlier Resistant Hierarchical Clustering

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-genieclust 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-stats 
Requires:         R-CRAN-genieclust 

%description
Includes the reference implementation of Genie - a hierarchical clustering
algorithm that links two point groups in such a way that an inequity
measure (namely, the Gini index) of the cluster sizes does not
significantly increase above a given threshold. This method most often
outperforms many other data segmentation approaches in terms of clustering
quality as tested on a wide range of benchmark datasets. At the same time,
Genie retains the high speed of the single linkage approach, therefore it
is also suitable for analysing larger data sets. For more details see
(Gagolewski et al. 2016 <DOI:10.1016/j.ins.2016.05.003>). For an even
faster and more feature-rich implementation, including, amongst others,
noise point detection, see the 'genieclust' package.

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
