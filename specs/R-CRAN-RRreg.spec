%global packname  RRreg
%global packver   0.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1
Release:          2%{?dist}
Summary:          Correlation and Regression Analyses for Randomized Response Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-lme4 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-lme4 

%description
Univariate and multivariate methods to analyze randomized response (RR)
survey designs (e.g., Warner, S. L. (1965). Randomized response: A survey
technique for eliminating evasive answer bias. Journal of the American
Statistical Association, 60, 63–69, <doi:10.2307/2283137>). Besides
univariate estimates of true proportions, RR variables can be used for
correlations, as dependent variable in a logistic regression (with or
without random effects), or as predictors in a linear regression (Heck, D.
W., & Moshagen, M. (2018). RRreg: An R package for correlation and
regression analyses of randomized response data. Journal of Statistical
Software, 85(2), 1–29, <doi:10.18637/jss.v085.i02>). For simulations and
the estimation of statistical power, RR data can be generated according to
several models. The implemented methods also allow to test the link
between continuous covariates and dishonesty in cheating paradigms such as
the coin-toss or dice-roll task (Moshagen, M., & Hilbig, B. E. (2017). The
statistical analysis of cheating paradigms. Behavior Research Methods, 49,
724–732, <doi:10.3758/s13428-016-0729-x>).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
