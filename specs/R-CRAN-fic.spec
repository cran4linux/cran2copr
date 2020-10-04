%global packname  fic
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Focused Information Criteria for Model Comparison

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-tensor 
BuildRequires:    R-CRAN-abind 
Requires:         R-stats 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-survival 
Requires:         R-CRAN-tensor 
Requires:         R-CRAN-abind 

%description
Compares how well different models estimate a quantity of interest (the
"focus") so that different models may be preferred for different purposes.
Comparisons within any class of models fitted by maximum likelihood are
supported, with shortcuts for commonly-used classes such as generalised
linear models and parametric survival models.  The methods originate from
Claeskens and Hjort (2003) <doi:10.1198/016214503000000819> and Claeskens
and Hjort (2008, ISBN:9780521852258).

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
