%global packname  ldamatch
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          2%{?dist}
Summary:          Selection of Statistically Similar Research Groups

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-RUnit 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-entropy 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-iterpc 
BuildRequires:    R-CRAN-kSamples 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-utils 
Requires:         R-MASS 
Requires:         R-CRAN-RUnit 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-entropy 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-iterpc 
Requires:         R-CRAN-kSamples 
Requires:         R-stats 
Requires:         R-CRAN-car 
Requires:         R-CRAN-gmp 
Requires:         R-utils 

%description
Select statistically similar research groups by backward selection using
various robust algorithms, including a heuristic based on linear
discriminant analysis, multiple heuristics based on the test statistic,
and parallelized exhaustive search.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
