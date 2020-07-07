%global packname  indirect
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}
Summary:          Elicitation of Independent Conditional Means Priors forGeneralised Linear Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-gplots 
Requires:         R-MASS 
Requires:         R-CRAN-gplots 

%description
Functions are provided to facilitate prior elicitation for Bayesian
generalised linear models using independent conditional means priors. The
package supports the elicitation of multivariate normal priors for
generalised linear models. The approach can be applied to indirect
elicitation for a generalised linear model that is linear in the
parameters. The package is designed such that the facilitator executes
functions within the R console during the elicitation session to provide
graphical and numerical feedback at each design point. Various
methodologies for eliciting fractiles (equivalently, percentiles or
quantiles) are supported, including versions of the approach of Hosack et
al. (2017) <doi:10.1016/j.ress.2017.06.011>. For example, experts may be
asked to provide central credible intervals that correspond to a certain
probability. Or experts may be allowed to vary the probability allocated
to the central credible interval for each design point. Additionally, a
median may or may not be elicited.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
