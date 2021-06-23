%global __brp_check_rpaths %{nil}
%global packname  latte
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Interface to 'LattE' and '4ti2'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         4ti2
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-mpoly 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-mpoly 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-glue 

%description
Back-end connections to 'LattE' (<https://www.math.ucdavis.edu/~latte>)
for counting lattice points and integration inside convex polytopes and
'4ti2' (<http://www.4ti2.de/>) for algebraic, geometric, and combinatorial
problems on linear spaces and front-end tools facilitating their use in
the 'R' ecosystem.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/INSTALL.txt
%{rlibdir}/%{packname}/INDEX
