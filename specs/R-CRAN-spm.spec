%global __brp_check_rpaths %{nil}
%global packname  spm
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Predictive Modeling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-psy 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-biomod2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ranger 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-psy 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-biomod2 
Requires:         R-stats 
Requires:         R-CRAN-ranger 

%description
Introduction to some novel accurate hybrid methods of geostatistical and
machine learning methods for spatial predictive modelling. It contains two
commonly used geostatistical methods, two machine learning methods, four
hybrid methods and two averaging methods. For each method, two functions
are provided. One function is for assessing the predictive errors and
accuracy of the method based on cross-validation. The other one is for
generating spatial predictions using the method. For details please see:
Li, J., Potter, A., Huang, Z., Daniell, J. J. and Heap, A. (2010)
<https:www.ga.gov.au/metadata-gateway/metadata/record/gcat_71407> Li, J.,
Heap, A. D., Potter, A., Huang, Z. and Daniell, J. (2011)
<doi:10.1016/j.csr.2011.05.015> Li, J., Heap, A. D., Potter, A. and
Daniell, J. (2011) <doi:10.1016/j.envsoft.2011.07.004> Li, J., Potter, A.,
Huang, Z. and Heap, A. (2012)
<https:www.ga.gov.au/metadata-gateway/metadata/record/74030>.

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
