%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DPpack
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Differentially Private Statistical Analysis and Machine Learning

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.51.6
BuildRequires:    R-stats >= 4.0.2
BuildRequires:    R-graphics >= 4.0.2
BuildRequires:    R-CRAN-ggplot2 >= 3.3.2
BuildRequires:    R-CRAN-R6 >= 2.5.1
BuildRequires:    R-CRAN-Rdpack >= 2.1.2
BuildRequires:    R-CRAN-e1071 >= 1.7.9
BuildRequires:    R-CRAN-nloptr >= 1.2.2.2
BuildRequires:    R-CRAN-rmutil >= 1.1.5
BuildRequires:    R-CRAN-dplyr >= 1.0.1
Requires:         R-CRAN-MASS >= 7.3.51.6
Requires:         R-stats >= 4.0.2
Requires:         R-graphics >= 4.0.2
Requires:         R-CRAN-ggplot2 >= 3.3.2
Requires:         R-CRAN-R6 >= 2.5.1
Requires:         R-CRAN-Rdpack >= 2.1.2
Requires:         R-CRAN-e1071 >= 1.7.9
Requires:         R-CRAN-nloptr >= 1.2.2.2
Requires:         R-CRAN-rmutil >= 1.1.5
Requires:         R-CRAN-dplyr >= 1.0.1

%description
An implementation of common statistical analysis and models with
differential privacy (Dwork et al., 2006a) <doi:10.1007/11681878_14>
guarantees. The package contains, for example, functions providing
differentially private computations of mean, variance, median, histograms,
and contingency tables. It also implements some statistical models and
machine learning algorithms such as linear regression (Kifer et al., 2012)
<https://proceedings.mlr.press/v23/kifer12.html> and SVM (Chaudhuri et
al., 2011) <https://jmlr.org/papers/v12/chaudhuri11a.html>. In addition,
it implements some popular randomization mechanisms, including the Laplace
mechanism (Dwork et al., 2006a) <doi:10.1007/11681878_14>, Gaussian
mechanism (Dwork et al., 2006b) <doi:10.1007/11761679_29>, analytic
Gaussian mechanism (Balle & Wang, 2018)
<https://proceedings.mlr.press/v80/balle18a.html>, and exponential
mechanism (McSherry & Talwar, 2007) <doi:10.1109/FOCS.2007.66>.

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
