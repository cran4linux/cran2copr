%global packname  longpower
%global packver   1.0-21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.21
Release:          3%{?dist}
Summary:          Sample Size Calculations for Longitudinal Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 >= 1.0
BuildRequires:    R-nlme 
Requires:         R-CRAN-lme4 >= 1.0
Requires:         R-nlme 

%description
Compute power and sample size for linear models of longitudinal data.
Supported models include mixed-effects models and models fit by
generalized least squares and generalized estimating equations. Relevant
formulas are derived by Liu and Liang (1997) <DOI:10.2307/2533554>, Diggle
et al (2002) <ISBN:9780199676750>, and Lu, Luo, and Chen (2008)
<DOI:10.2202/1557-4679.1098>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
