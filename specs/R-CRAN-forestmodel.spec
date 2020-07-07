%global packname  forestmodel
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          3%{?dist}
Summary:          Forest Plots from Regression Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-tibble >= 1.4.2
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-broom >= 0.4.4
BuildRequires:    R-CRAN-lazyeval >= 0.1.10
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-tibble >= 1.4.2
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-broom >= 0.4.4
Requires:         R-CRAN-lazyeval >= 0.1.10

%description
Produces forest plots using 'ggplot2' from models produced by functions
such as stats::lm(), stats::glm() and survival::coxph().

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
