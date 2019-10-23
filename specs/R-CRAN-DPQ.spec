%global packname  DPQ
%global packver   0.3-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.5
Release:          1%{?dist}
Summary:          Density, Probability, Quantile ('DPQ') Computations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-sfsmisc 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-sfsmisc 

%description
Computations for approximations and alternatives for the 'DPQ' (Density
(pdf), Probability (cdf) and Quantile) functions for probability
distributions in R. Primary focus is on (central and non-central) beta,
gamma and related distributions such as the chi-squared, F, and t. -- This
is for the use of researchers in these numerical approximation
implementations, notably for my own use in order to improve R`s own
pbeta(), qgamma(), ..., etc: {'"dpq"'-functions}. -- We plan to complement
with 'DPQmpfr' to be suggested later.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/safe
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
