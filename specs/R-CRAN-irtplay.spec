%global packname  irtplay
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}
Summary:          Evaluation of Model-Data Fit in Item Response Theory (IRT) andUseful Functions Related to IRT

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbapply 
Requires:         R-stats 
Requires:         R-CRAN-statmod 
Requires:         R-utils 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-gridExtra 
Requires:         R-parallel 
Requires:         R-CRAN-pbapply 

%description
Examine the IRT model-data fit on item-level in different ways as well as
provide useful functions related to unidimensional item response theory
(IRT). In terms of assessing the IRT model-data fit, one of distinguished
features of this package is that it gives not only well-known item fit
statistics (e.g., chi-square (X2), likelihood ratio chi-square (G2), infit
and oufit statistics (Ames & Penfield (2015) <doi:10.1111/emip.12067>))
but also graphical displays to look at residuals between between the
observed data and model-based predictions (Hambleton, Swaminathan, &
Rogers (1991, ISBN:9780803936478)). More evaluation methods will be
included in the future updated version. In addition to the evaluation of
IRT model-data fit, there are several useful functions such as estimating
proficiency parameters, calibrating item parameters given the fixed
effects (aka. ability values) (Baker & Kim (2004, ISBN:9780824758257)),
computing asymptotic variance-covariance matrices of item parameter
estimates (Li & Lissitz (2004) <doi:10.1111/j.1745-3984.2004.tb01109.x>),
importing item and/or ability parameters from popular IRT software,
generating simulated data, computing the conditional distribution of
observed scores using the Lord-Wingersky recursion formula (Lord &
Wingersky (1984) <doi:10.1207/s15324818ame1002_1>), computing the
loglikelihood of individual items, computing the loglikelihood of
abilities, computing item and test information functions, computing item
and test characteristic curve functions, and plotting item and test
characteristic curves and item and test information functions.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
