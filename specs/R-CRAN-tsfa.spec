%global packname  tsfa
%global packver   2014.10-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2014.10.1
Release:          2%{?dist}
Summary:          Time Series Factor Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.1.0
Requires:         R-core >= 2.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tfplot >= 2014.2.1
BuildRequires:    R-CRAN-tframe >= 2011.3.1
BuildRequires:    R-CRAN-GPArotation >= 2006.9.1
BuildRequires:    R-CRAN-dse >= 2006.1.1
BuildRequires:    R-CRAN-EvalEst >= 2006.1.1
BuildRequires:    R-CRAN-setRNG >= 2004.4.1
Requires:         R-CRAN-tfplot >= 2014.2.1
Requires:         R-CRAN-tframe >= 2011.3.1
Requires:         R-CRAN-GPArotation >= 2006.9.1
Requires:         R-CRAN-dse >= 2006.1.1
Requires:         R-CRAN-EvalEst >= 2006.1.1
Requires:         R-CRAN-setRNG >= 2004.4.1

%description
Extraction of Factors from Multivariate Time Series. See ?00tsfa-Intro for
more details.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
