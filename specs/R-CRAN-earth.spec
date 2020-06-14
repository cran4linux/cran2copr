%global packname  earth
%global packver   5.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.1.2
Release:          2%{?dist}
Summary:          Multivariate Adaptive Regression Splines

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-plotmo >= 3.5.4
BuildRequires:    R-CRAN-TeachingDemos >= 2.10
BuildRequires:    R-CRAN-Formula >= 1.2.3
Requires:         R-CRAN-plotmo >= 3.5.4
Requires:         R-CRAN-TeachingDemos >= 2.10
Requires:         R-CRAN-Formula >= 1.2.3

%description
Build regression models using the techniques in Friedman's papers "Fast
MARS" and "Multivariate Adaptive Regression Splines"
<doi:10.1214/aos/1176347963>. (The term "MARS" is trademarked and thus not
used in the name of the package.)

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/slowtests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
