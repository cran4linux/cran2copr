%global packname  cmprsk
%global packver   2.2-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.9
Release:          1%{?dist}
Summary:          Subdistribution Analysis of Competing Risks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-survival 
Requires:         R-survival 

%description
Estimation, testing and regression modeling of subdistribution functions
in competing risks, as described in Gray (1988), A class of K-sample tests
for comparing the cumulative incidence of a competing risk, Ann. Stat.
16:1141-1154 <DOI:10.1214/aos/1176350951>, and Fine JP and Gray RJ (1999),
A proportional hazards model for the subdistribution of a competing risk,
JASA, 94:496-509, <DOI:10.1080/01621459.1999.10474144>.

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
%{rlibdir}/%{packname}/libs
