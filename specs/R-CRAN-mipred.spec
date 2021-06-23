%global __brp_check_rpaths %{nil}
%global packname  mipred
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Prediction using Multiple Imputation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mice >= 3.4.0
Requires:         R-CRAN-mice >= 3.4.0

%description
Calibration of generalized linear models and Cox regression models for
prediction using multiple imputation to account for missing values in the
predictors as described in the paper by "Mertens, Banzato and de Wreede"
(2018) <arXiv:1810.05099>. The methodology and calculations described in
this paper are fully implemented in this package. The vignette describes
all data analytic steps which allow users to replicate results using the
package functions on the data analyzed in the paper or on their own data.
Imputations are generated using the package 'mice' without using the
outcomes of observations for which the predictions are generated. Two
options are provided to generate predictions. The first is
prediction-averaging of predictions calibrated from single models fitted
on single imputed datasets within a set of multiple imputations. The
second is application of the Rubin's rules pooled model. For both
implementations, unobserved values in the predictor data of new
observations for which the predictions are derived are automatically
imputed. The package contains two basic functions. The first, mipred()
generates predictions of outcome on new observations. The second,
mipred.cv() generates cross-validated predictions with the methodology on
existing data for which outcomes have already been observed. The present
version is still in development and should support continuous, binary and
counting outcomes, but we have only thoroughly checked performance for
binary outcome logistic regression modeling. We will include the Cox
regression extension later.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
