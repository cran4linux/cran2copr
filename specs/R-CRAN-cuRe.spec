%global packname  cuRe
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          2%{?dist}
Summary:          Parametric Cure Model Estimation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-rstpm2 
BuildRequires:    R-CRAN-date 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-relsurv 
Requires:         R-survival 
Requires:         R-CRAN-rstpm2 
Requires:         R-CRAN-date 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-relsurv 

%description
Contains functions for estimating generalized parametric mixture and
non-mixture cure models, loss of lifetime, mean residual lifetime, and
crude event probabilities.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/calc.Crude.ex.R
%doc %{rlibdir}/%{packname}/calc.Crude.quantile.ex.R
%doc %{rlibdir}/%{packname}/calc.cure.quantile.ex.R
%doc %{rlibdir}/%{packname}/calc.LL.ex.R
%doc %{rlibdir}/%{packname}/calc.LL.quantile.ex.R
%doc %{rlibdir}/%{packname}/fit.cure.model.ex.R
%doc %{rlibdir}/%{packname}/FlexCureModel.ex.R
%doc %{rlibdir}/%{packname}/general.haz.ex.R
%doc %{rlibdir}/%{packname}/GenFlexCureModel.ex.R
%doc %{rlibdir}/%{packname}/predict.lts.ex.R
%{rlibdir}/%{packname}/INDEX
