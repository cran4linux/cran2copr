%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  l1penSVMs
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Regularization Paths of L1-Penalized SVMs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-fastDummies 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-fastDummies 
Requires:         R-CRAN-MASS 

%description
Computes regularization paths for L1-penalized support vector machine
(SVM) models, including the standard SVM, receiver operating
characteristic SVM (ROC-SVM), and fraud detection SVM (FD-SVM). The
package implements efficient path algorithms to obtain solutions over a
wide range of regularization parameter values. It also provides
cross-validation for selecting an optimal regularization parameter, along
with functions for prediction, visualization, and summarization of the
fitted models. For more details, see Zhu et al. (2003)
<https://proceedings.neurips.cc/paper_files/paper/2003/file/49d4b2faeb4b7b9e745775793141e2b2-Paper.pdf>,
Kim et al. (2021) <doi:10.1002/sta4.400>, Park et al. (2023)
<doi:10.1007/s42952-023-00207-6>.

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
