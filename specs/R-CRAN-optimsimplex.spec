%global packname  optimsimplex
%global packver   1.0-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          1%{?dist}
Summary:          R Port of the 'Scilab' Optimsimplex Module

License:          CeCILL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-optimbase >= 1.0.8
BuildRequires:    R-methods 
Requires:         R-CRAN-optimbase >= 1.0.8
Requires:         R-methods 

%description
Provides a building block for optimization algorithms based on a simplex.
The 'optimsimplex' package may be used in the following optimization
methods: the simplex method of Spendley et al. (1962)
<doi:10.1080/00401706.1962.10490033>, the method of Nelder and Mead (1965)
<doi:10.1093/comjnl/7.4.308>, Box's algorithm for constrained optimization
(1965) <doi:10.1093/comjnl/8.1.42>, the multi-dimensional search by
Torczon (1989) <http://www.cs.wm.edu/~va/research/thesis.pdf>, etc...

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
