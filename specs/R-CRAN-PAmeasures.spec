%global packname  PAmeasures
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Prediction and Accuracy Measures for Nonlinear Models and forRight-Censored Time-to-Event Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-stats 
Requires:         R-survival 
Requires:         R-stats 

%description
We propose a pair of summary measures for the predictive power of a
prediction function based on a regression model. The regression model can
be linear or nonlinear, parametric, semi-parametric, or nonparametric, and
correctly specified or mis-specified. The first measure, R-squared, is an
extension of the classical R-squared statistic for a linear model,
quantifying the prediction function's ability to capture the variability
of the response. The second measure, L-squared, quantifies the prediction
function's bias for predicting the mean regression function. When used
together, they give a complete summary of the predictive power of a
prediction function. Please refer to Gang Li and Xiaoyan Wang (2016)
<arXiv:1611.03063> for more details.

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
