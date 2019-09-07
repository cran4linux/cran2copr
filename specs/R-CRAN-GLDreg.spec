%global packname  GLDreg
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          1%{?dist}
Summary:          Fit GLD Regression Model and GLD Quantile Regression Model toEmpirical Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-GLDEX >= 2.0.0.5
BuildRequires:    R-CRAN-ddst 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-GLDEX >= 2.0.0.5
Requires:         R-CRAN-ddst 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 

%description
Owing to the rich shapes of Generalised Lambda Distributions (GLDs), GLD
standard/quantile regression is a competitive flexible model compared to
standard/quantile regression.  The proposed method has some major
advantages: 1) it provides a reference line which is very robust to
outliers with the attractive property of zero mean residuals and 2) it
gives a unified, elegant quantile regression model from the reference line
with smooth regression coefficients across different quantiles. The
goodness of fit of the proposed model can be assessed via QQ plots and
Kolmogorov-Smirnov tests and data driven smooth test, to ensure the
appropriateness of the statistical inference under consideration.
Statistical distributions of coefficients of the GLD regression line are
obtained using simulation, and interval estimates are obtained directly
from simulated data.

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
%{rlibdir}/%{packname}/INDEX
