%global packname  sgmodel
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Solves a Generic Stochastic Growth Model with a RepresentativeAgent

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ramify 
BuildRequires:    R-CRAN-Rtauchen 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ramify 
Requires:         R-CRAN-Rtauchen 

%description
It computes the solutions to a generic stochastic growth model for a given
set of user supplied parameters. It includes the solutions to the model,
plots of the solution, a summary of the features of the model, a function
that covers different types of consumption preferences, and a function
that computes the moments of a Markov process. Merton, Robert C (1971)
<doi:10.1016/0022-0531(71)90038-X>, Tauchen, George (1986)
<doi:10.1016/0165-1765(86)90168-0>, Wickham, Hadley (2009,
ISBN:978-0-387-98140-6 ).

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
