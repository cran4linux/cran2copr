%global packname  condir
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Computation of P Values and Bayes Factors for Conditioning Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.3.2
BuildRequires:    R-graphics >= 3.3.2
BuildRequires:    R-CRAN-psych >= 1.9.12
BuildRequires:    R-CRAN-xtable >= 1.8.2
BuildRequires:    R-CRAN-shiny >= 1.4.0
BuildRequires:    R-CRAN-knitr >= 1.28
BuildRequires:    R-CRAN-BayesFactor >= 0.9.12
BuildRequires:    R-CRAN-effsize >= 0.7.8
Requires:         R-stats >= 3.3.2
Requires:         R-graphics >= 3.3.2
Requires:         R-CRAN-psych >= 1.9.12
Requires:         R-CRAN-xtable >= 1.8.2
Requires:         R-CRAN-shiny >= 1.4.0
Requires:         R-CRAN-knitr >= 1.28
Requires:         R-CRAN-BayesFactor >= 0.9.12
Requires:         R-CRAN-effsize >= 0.7.8

%description
Set of functions for the easy analyses of conditioning data.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/app
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
