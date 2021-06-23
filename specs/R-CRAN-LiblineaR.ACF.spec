%global __brp_check_rpaths %{nil}
%global packname  LiblineaR.ACF
%global packver   1.94-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.94.2
Release:          3%{?dist}%{?buildtag}
Summary:          Linear Classification with Online Adaptation of CoordinateFrequencies

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
Solving the linear SVM problem with coordinate descent is very efficient
and is implemented in one of the most often used packages, 'LIBLINEAR'
(available at http://www.csie.ntu.edu.tw/~cjlin/liblinear). It has been
shown that the uniform selection of coordinates can be accelerated by
using an online adaptation of coordinate frequencies (ACF). This package
implements ACF and is based on 'LIBLINEAR' as well as the 'LiblineaR'
package (<https://cran.r-project.org/package=LiblineaR>). It currently
supports L2-regularized L1-loss as well as L2-loss linear SVM. Similar to
'LIBLINEAR' multi-class classification (one-vs-the rest, and Crammer &
Singer method) and cross validation for model selection is supported. The
training of the models based on ACF is much faster than standard
'LIBLINEAR' on many problems.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
