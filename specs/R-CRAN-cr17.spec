%global packname  cr17
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Testing Differences Between Competing Risks Models and TheirVisualisations

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.2
Requires:         R-core >= 3.3.2
BuildArch:        noarch
BuildRequires:    R-grid >= 3.3.0
BuildRequires:    R-survival >= 2.41.3
BuildRequires:    R-CRAN-cmprsk >= 2.2.7
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-gridExtra >= 2.2.1
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-scales >= 0.4.1
BuildRequires:    R-CRAN-gtable >= 0.2.0
Requires:         R-grid >= 3.3.0
Requires:         R-survival >= 2.41.3
Requires:         R-CRAN-cmprsk >= 2.2.7
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-gridExtra >= 2.2.1
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-scales >= 0.4.1
Requires:         R-CRAN-gtable >= 0.2.0

%description
Tool for analyzing competing risks models. The main point of interest is
testing differences between groups (as described in R.J Gray (1988)
<doi:10.1214/aos/1176350951> and J.P. Fine, R.J Gray (1999)
<doi:10.2307/2670170>) and visualizations of survival and cumulative
incidence curves.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
