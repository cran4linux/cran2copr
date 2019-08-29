%global packname  MLEcens
%global packver   0.1-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          Computation of the MLE for bivariate (interval) censored data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
This package contains functions to compute the nonparametric maximum
likelihood estimator (MLE) for the bivariate distribution of (X,Y), when
realizations of (X,Y) cannot be observed directly.  To be more precise, we
consider the situation where we observe a set of rectangles that are known
to contain the unobservable realizations of (X,Y). We compute the MLE
based on such a set of rectangles.  The methods can also be used for
univariate censored data (see data set 'cosmesis'), and for censored data
with competing risks (see data set 'menopause').  We also provide
functions to visualize the observed data and the MLE.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
