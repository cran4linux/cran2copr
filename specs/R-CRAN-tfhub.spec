%global __brp_check_rpaths %{nil}
%global packname  tfhub
%global packver   0.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.1
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to 'TensorFlow' Hub

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate >= 1.9.9002
BuildRequires:    R-CRAN-tensorflow >= 1.8.0.9006
BuildRequires:    R-CRAN-rstudioapi >= 0.7
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-vctrs 
Requires:         R-CRAN-reticulate >= 1.9.9002
Requires:         R-CRAN-tensorflow >= 1.8.0.9006
Requires:         R-CRAN-rstudioapi >= 0.7
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-vctrs 

%description
'TensorFlow' Hub is a library for the publication, discovery, and
consumption of reusable parts of machine learning models. A module is a
self-contained piece of a 'TensorFlow' graph, along with its weights and
assets, that can be reused across different tasks in a process known as
transfer learning. Transfer learning train a model with a smaller dataset,
improve generalization, and speed up training.

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
