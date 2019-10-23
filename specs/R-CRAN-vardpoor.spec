%global packname  vardpoor
%global packver   0.16.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.16.0
Release:          1%{?dist}
Summary:          Variance Estimation for Sample Surveys by the Ultimate ClusterMethod

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildRequires:    R-CRAN-data.table >= 1.11.4
BuildRequires:    R-CRAN-laeken 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-surveyplanning 
Requires:         R-CRAN-data.table >= 1.11.4
Requires:         R-CRAN-laeken 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pracma 
Requires:         R-graphics 
Requires:         R-CRAN-plyr 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-surveyplanning 

%description
Generation of domain variables, linearization of several nonlinear
population statistics (the ratio of two totals, weighted income
percentile, relative median income ratio, at-risk-of-poverty rate,
at-risk-of-poverty threshold, Gini coefficient, gender pay gap, the
aggregate replacement ratio, the relative median income ratio, median
income below at-risk-of-poverty gap, income quintile share ratio, relative
median at-risk-of-poverty gap), computation of regression residuals in
case of weight calibration, variance estimation of sample surveys by the
ultimate cluster method (Hansen, Hurwitz and Madow,Theory, vol. I: Methods
and Applications; vol. II: Theory. 1953, New York: John Wiley and Sons),
variance estimation for longitudinal, cross-sectional measures and
measures of change for single and multistage stage cluster sampling
designs (Berger, Y. G., 2015, <doi:10.1111/rssa.12116>). Several other
precision measures are derived - standard error, the coefficient of
variation, the margin of error, confidence interval, design effect.

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
%doc %{rlibdir}/%{packname}/BUGS
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/COPYING
%doc %{rlibdir}/%{packname}/DISCLAIMER
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/README
%{rlibdir}/%{packname}/INDEX
