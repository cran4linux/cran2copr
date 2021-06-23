%global __brp_check_rpaths %{nil}
%global packname  denpro
%global packver   0.9.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.2
Release:          3%{?dist}%{?buildtag}
Summary:          Visualization of Multivariate Functions, Sets, and Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
We provide tools to (1) visualize multivariate density functions and
density estimates with level set trees, (2) visualize level sets with
shape trees, (3) visualize multivariate data with tail trees, (4)
visualize scales of multivariate density estimates with mode graphs and
branching maps, and (5) visualize anisotropic spread with 2D volume
functions and 2D probability content functions. Level set trees visualize
mode structure, shape trees visualize shapes of level sets of unimodal
densities, and tail trees visualize connected data sets. The kernel
estimator is implemented but the package may also be applied for
visualizing other density estimates.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
