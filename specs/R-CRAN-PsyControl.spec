%global packname  PsyControl
%global packver   1.0.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          CUSUM Person Fit Statistics

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.3
Requires:         R-core >= 3.3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-ltm 
BuildRequires:    R-CRAN-irtoys 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-ltm 
Requires:         R-CRAN-irtoys 
Requires:         R-stats 
Requires:         R-graphics 

%description
Person fit statistics based on Quality Control measures are provided for
questionnaires and tests given a specified IRT model. Statistics based on
Cumulative Sum (CUSUM) charts are provided. Options are given for banks
with polytomous and dichotomous data.

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
%{rlibdir}/%{packname}/INDEX
