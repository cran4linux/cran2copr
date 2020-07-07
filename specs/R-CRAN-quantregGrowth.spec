%global packname  quantregGrowth
%global packver   0.4-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          3%{?dist}
Summary:          Growth Charts via Regression Quantiles

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-splines 
Requires:         R-CRAN-quantreg 
Requires:         R-splines 

%description
Fits non-crossing regression quantiles as a function of linear covariates
and multiple smooth terms via B-splines with L1-norm difference penalties.
Monotonicity constraints on the fitted curves are allowed. See Muggeo,
Sciandra, Tomasello and Calvo (2013) <doi:10.1007/s10651-012-0232-1> and
<doi:10.13140/RG.2.2.12924.85122> for some code example.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
