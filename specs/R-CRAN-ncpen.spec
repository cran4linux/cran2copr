%global packname  ncpen
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Unified Algorithm for Non-convex Penalized Estimation forGeneralized Linear Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.11.2

%description
An efficient unified nonconvex penalized estimation algorithm for Gaussian
(linear), binomial Logit (logistic), Poisson, multinomial Logit, and Cox
proportional hazard regression models. The unified algorithm is
implemented based on the convex concave procedure and the algorithm can be
applied to most of the existing nonconvex penalties. The algorithm also
supports convex penalty: least absolute shrinkage and selection operator
(LASSO). Supported nonconvex penalties include smoothly clipped absolute
deviation (SCAD), minimax concave penalty (MCP), truncated LASSO penalty
(TLP), clipped LASSO (CLASSO), sparse ridge (SRIDGE), modified bridge
(MBRIDGE) and modified log (MLOG). For high-dimensional data (data set
with many variables), the algorithm selects relevant variables producing a
parsimonious regression model. Kim, D., Lee, S. and Kwon, S. (2018)
<arXiv:1811.05061>, Lee, S., Kwon, S. and Kim, Y. (2016)
<doi:10.1016/j.csda.2015.08.019>, Kwon, S., Lee, S. and Kim, Y. (2015)
<doi:10.1016/j.csda.2015.07.001>. (This research is funded by Julian
Virtue Professorship from Center for Applied Research at Pepperdine
Graziadio Business School and the National Research Foundation of Korea.)

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
