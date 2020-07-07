%global packname  AnnuityRIR
%global packver   1.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Annuity Random Interest Rates

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.5
Requires:         R-core >= 3.2.5
BuildArch:        noarch
BuildRequires:    R-CRAN-mc2d 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-EnvStats 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-stats 
Requires:         R-CRAN-mc2d 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-EnvStats 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-actuar 
Requires:         R-stats 

%description
Annuity Random Interest Rates proposes different techniques for the
approximation of the present and final value of a unitary annuity-due or
annuity-immediate considering interest rate as a random variable. Cruz
Rambaud et al. (2017) <doi:10.1007/978-3-319-54819-7_16>. Cruz Rambaud et
al. (2015) <doi:10.23755/rm.v28i1.25>.

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
