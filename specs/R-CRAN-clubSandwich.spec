%global packname  clubSandwich
%global packver   0.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.5
Release:          1%{?dist}
Summary:          Cluster-Robust (Sandwich) Variance Estimators with Small-SampleCorrections

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sandwich 
Requires:         R-stats 
Requires:         R-CRAN-sandwich 

%description
Provides several cluster-robust variance estimators (i.e., sandwich
estimators) for ordinary and weighted least squares linear regression
models, including the bias-reduced linearization estimator introduced by
Bell and McCaffrey (2002)
<http://www.statcan.gc.ca/pub/12-001-x/2002002/article/9058-eng.pdf> and
developed further by Pustejovsky and Tipton (2017)
<DOI:10.1080/07350015.2016.1247004>. The package includes functions for
estimating the variance- covariance matrix and for testing single- and
multiple- contrast hypotheses based on Wald test statistics. Tests of
single regression coefficients use Satterthwaite or saddle-point
corrections. Tests of multiple- contrast hypotheses use an approximation
to Hotelling's T-squared distribution. Methods are provided for a variety
of fitted models, including lm() and mlm objects, glm(), ivreg() (from
package 'AER'), plm() (from package 'plm'), gls() and lme() (from 'nlme'),
robu() (from 'robumeta'), and rma.uni() and rma.mv() (from 'metafor').

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
