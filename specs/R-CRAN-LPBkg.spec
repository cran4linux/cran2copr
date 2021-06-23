%global __brp_check_rpaths %{nil}
%global packname  LPBkg
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Detecting New Signals under Background Mismodelling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.1
Requires:         R-core >= 2.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-polynom 
BuildRequires:    R-CRAN-orthopolynom 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-polynom 
Requires:         R-CRAN-orthopolynom 
Requires:         R-CRAN-Hmisc 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 

%description
Given a postulated model and a set of data, the comparison density is
estimated and the deviance test is implemented in order to assess if the
data distribution deviates significantly from the postulated model.
Finally, the results are summarized in a CD-plot as described in Algeri S.
(2019) <arXiv:1906.06615>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
