%global packname  pseudo
%global packver   1.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.3
Release:          3%{?dist}%{?buildtag}
Summary:          Computes Pseudo-Observations for Modeling

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.3
Requires:         R-core >= 3.3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-KMsurv 
BuildRequires:    R-CRAN-geepack 
Requires:         R-CRAN-KMsurv 
Requires:         R-CRAN-geepack 

%description
Various functions for computing pseudo-observations for censored data
regression. Computes pseudo-observations for modeling: competing risks
based on the cumulative incidence function, survival function based on the
restricted mean, survival function based on the Kaplan-Meier estimator see
Klein et al. (2008) <doi:10.1016/j.cmpb.2007.11.017>.

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
