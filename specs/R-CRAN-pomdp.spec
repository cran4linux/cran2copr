%global packname  pomdp
%global packver   0.99.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.99.0
Release:          2%{?dist}
Summary:          Solver for Partially Observable Markov Decision Processes(POMDP)

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-Ternary 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-Ternary 

%description
Provides the infrastructure to define and analyze the solutions of
Partially Observable Markov Decision Processes (POMDP) models. The package
includes pomdp-solve to solve POMDPs using a variety of exact and
approximate value iteration algorithms. Smallwood and Sondik (1973)
<doi:10.1287/opre.21.5.1071>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/pomdp-solve
