%global __brp_check_rpaths %{nil}
%global packname  sboost
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Machine Learning with AdaBoost on Decision Stumps

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-stats >= 3.4
BuildRequires:    R-CRAN-dplyr >= 0.7.6
BuildRequires:    R-CRAN-rlang >= 0.2.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.17
Requires:         R-stats >= 3.4
Requires:         R-CRAN-dplyr >= 0.7.6
Requires:         R-CRAN-rlang >= 0.2.1
Requires:         R-CRAN-Rcpp >= 0.12.17

%description
Creates classifier for binary outcomes using Adaptive Boosting (AdaBoost)
algorithm on decision stumps with a fast C++ implementation. For a
description of AdaBoost, see Freund and Schapire (1997)
<doi:10.1006/jcss.1997.1504>. This type of classifier is nonlinear, but
easy to interpret and visualize. Feature vectors may be a combination of
continuous (numeric) and categorical (string, factor) elements. Methods
for classifier assessment, predictions, and cross-validation also
included.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
