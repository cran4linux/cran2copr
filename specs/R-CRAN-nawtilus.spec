%global packname  nawtilus
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          2%{?dist}
Summary:          Navigated Weighting for the Inverse Probability Weighting

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-MASS 
Requires:         R-MASS 

%description
Implements the navigated weighting (NAWT) proposed by Katsumata (2020)
<arXiv:2005.10998>, which improves the inverse probability weighting by
utilizing estimating equations suitable for a specific pre-specified
parameter of interest (e.g., the average treatment effects or the average
treatment effects on the treated) in propensity score estimation. It
includes the covariate balancing propensity score proposed by Imai and
Ratkovic (2014) <doi:10.1111/rssb.12027>, which uses covariate balancing
conditions in propensity score estimation. The point estimate of the
parameter of interest as well as coefficients for propensity score
estimation and their uncertainty are produced using the M-estimation. The
same functions can be used to estimate average outcomes in missing outcome
cases.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
