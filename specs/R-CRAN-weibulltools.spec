%global packname  weibulltools
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          2%{?dist}
Summary:          Statistical Methods for Life Data Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-LearnBayes 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-segmented 
BuildRequires:    R-CRAN-SPREDA 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-LearnBayes 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-Rcpp >= 0.12.18
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-segmented 
Requires:         R-CRAN-SPREDA 
Requires:         R-survival 

%description
Contains methods for examining bench test or field data using the
well-known Weibull Analysis. It includes Monte Carlo simulation for
estimating the life span of products that have not failed, taking account
of registering and reporting delays as stated in (Verband der
Automobilindustrie e.V. (VDA), 2016, <ISSN:0943-9412>). If the products
looked upon are vehicles, the covered mileage can be estimated as well. It
also provides non-parametric estimators like Median Ranks, Kaplan-Meier
(Abernethy, 2006, <ISBN:978-0-9653062-3-2>), Johnson (Johnson, 1964,
<ISBN:978-0444403223>), and Nelson-Aalen for failure probability
estimation within samples that contain failures as well as censored data.
Methods for estimating the parameters of lifetime distributions, like
Maximum Likelihood and Median-Rank Regression, (Genschel and Meeker, 2010,
<DOI:10.1080/08982112.2010.503447>) as well as the computation of
confidence intervals of quantiles and probabilities using the delta method
related to Fisher's confidence intervals (Meeker and Escobar, 1998,
<ISBN:9780471673279>) and the beta-binomial confidence bounds are also
included. If desired, the data can automatically be divided into subgroups
using segmented regression. And if the number of subgroups in a Weibull
Mixture Model is known, data can be analyzed using the EM-Algorithm.
Besides the calculation, methods for interactive visualization of the
edited data using *plotly* are provided as well. These visualizations
include the layout of a probability plot for a specified distribution, the
graphical technique of probability plotting and the possibility of adding
regression lines and confidence bounds to existing plots.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
