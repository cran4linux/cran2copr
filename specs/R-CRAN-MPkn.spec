%global __brp_check_rpaths %{nil}
%global packname  MPkn
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Calculations of One Discrete Model in Several Time Steps

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
A matrix discrete model having the form 'M[i+1] = (I + Q)*M[i]'. The
calculation of the values of 'M[i]' only for pre-selected values of 'i'.
The method of calculation is presented in the vignette 'Fundament'
('Base'). Maybe it`s own idea of the author of the package. A weakness is
that the method gives information only in selected steps of the process.
It mainly refers to cases with matrices that are not Markov chain. If 'Q'
is Markov transition matrix, then MUPkL() may be used to calculate the
steady-state distribution 'p' for 'p = Q*p'. Matrix power of non integer
(matrix.powerni()) gives the same results as a mpower() from package
'matlib'. References: "Markov chains",
(<https://en.wikipedia.org/wiki/Markov_chain#Expected_number_of_visits>).
Donald R. Burleson, Ph.D. (2005), "ON NON-INTEGER POWERS OF A SQUARE
MATRIX", (<http://www.blackmesapress.com/Eigenvalues.htm>).

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
%{rlibdir}/%{packname}/INDEX
