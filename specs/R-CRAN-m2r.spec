%global packname  m2r
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Interface to 'Macaulay2'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-mpoly >= 1.0.5
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-mpoly >= 1.0.5
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-gmp 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-Rcpp 

%description
Persistent interface to 'Macaulay2' <http://www.math.uiuc.edu/Macaulay2/>
and front-end tools facilitating its use in the 'R' ecosystem. For details
see Kahle et. al. (2020) <doi:10.18637/jss.v093.i09>.

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
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/server
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
