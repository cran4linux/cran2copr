%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GPUmatrix
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Basic Linear Algebra with GPU

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-stats 
Requires:         R-methods 

%description
GPUs are great resources for data analysis, especially in statistics and
linear algebra. Unfortunately, very few packages connect R to the GPU, and
none of them are transparent enough to run the computations on the GPU
without substantial changes to the code. The maintenance of these packages
is cumbersome: several of the earlier attempts have been removed from
their respective repositories. It would be desirable to have a properly
maintained R package that takes advantage of the GPU with minimal changes
to the existing code. We have developed the GPUmatrix package (available
on CRAN). GPUmatrix mimics the behavior of the Matrix package and extends
R to use the GPU for computations. It includes single(FP32) and
double(FP64) precision data types, and provides support for sparse
matrices. It is easy to learn, and requires very few code changes to
perform the operations on the GPU. GPUmatrix relies on either the Torch or
Tensorflow R packages to perform the GPU operations. We have demonstrated
its usefulness for several statistical applications and machine learning
applications: non-negative matrix factorization, logistic regression and
general linear models. We have also included a comparison of GPU and CPU
performance on different matrix operations.

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
