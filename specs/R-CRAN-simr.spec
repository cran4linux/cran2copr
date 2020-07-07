%global packname  simr
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          3%{?dist}
Summary:          Power Analysis for Generalised Linear Mixed Models by Simulation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 >= 1.1.16
BuildRequires:    R-CRAN-binom 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-pbkrtest 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-RLRsim 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-car 
Requires:         R-CRAN-lme4 >= 1.1.16
Requires:         R-CRAN-binom 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-pbkrtest 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-RLRsim 
Requires:         R-CRAN-stringr 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-car 

%description
Calculate power for generalised linear mixed models, using simulation.
Designed to work with models fit using the 'lme4' package. Described in
Green and MacLeod, 2016 <doi:10.1111/2041-210X.12504>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
