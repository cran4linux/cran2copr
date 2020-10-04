%global packname  kmi
%global packver   0.5.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.5
Release:          3%{?dist}%{?buildtag}
Summary:          Kaplan-Meier Multiple Imputation for the Analysis of CumulativeIncidence Functions in the Competing Risks Setting

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mitools 
BuildRequires:    R-survival 
BuildRequires:    R-stats 
Requires:         R-CRAN-mitools 
Requires:         R-survival 
Requires:         R-stats 

%description
Performs a Kaplan-Meier multiple imputation to recover the missing
potential censoring information from competing risks events, so that
standard right-censored methods could be applied to the imputed data sets
to perform analyses of the cumulative incidence functions (Allignol and
Beyersmann, 2010 <doi:10.1093/biostatistics/kxq018>).

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
