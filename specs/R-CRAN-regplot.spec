%global packname  regplot
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Enhanced Regression Nomogram Plot

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-vioplot 
BuildRequires:    R-CRAN-sm 
BuildRequires:    R-CRAN-beanplot 
BuildRequires:    R-survival 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lme4 
Requires:         R-CRAN-vioplot 
Requires:         R-CRAN-sm 
Requires:         R-CRAN-beanplot 
Requires:         R-survival 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-lme4 

%description
A function to plot a regression nomogram of regression objects. Covariate
distributions are superimposed on nomogram scales and the plot can be
animated to allow on-the-fly changes to distribution representation and to
enable outcome calculation.

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
