%global packname  BivRec
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Bivariate Alternating Recurrent Event Data Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-survival 
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-survival 
Requires:         R-stats 
Requires:         R-MASS 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-Rcpp 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Alternating recurrent event data arise frequently in biomedical and social
sciences where 2 types of events such as hospital admissions and discharge
occur alternatively over time. As such we implement a collection of
non-parametric and semiparametric methods to analyze such data. The main
functions are biv.rec.fit() and biv.rec.np(). Use biv.rec.fit() for
estimation of covariate effects on the two alternating event gap times
(xij and yij) using semiparametric methods. The method options are
"Lee.et.al" and "Chang". Use biv.rec.np() for estimation of the joint
cumulative distribution function (cdf) for the two alternating events gap
times (xij and yij) as well as the marginal survival function for type I
gap times (xij) and the conditional cdf of the type II gap times (yij)
given an interval of type I gap times (xij) in a non-parametric fashion.
The package also provides options to simulate and visualize the data and
results of analysis.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
