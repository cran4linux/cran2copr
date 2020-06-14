%global packname  estprod
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          2%{?dist}
Summary:          Estimation of Production Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-gmm 
Requires:         R-CRAN-lazyeval 
Requires:         R-boot 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-gmm 

%description
Estimation of production functions by the Olley-Pakes, Levinsohn-Petrin
and Wooldridge methodologies. The package aims to reproduce the results
obtained with the Stata's user written opreg
<http://www.stata-journal.com/article.html?article=st0145> and levpet
<http://www.stata-journal.com/article.html?article=st0060> commands. The
first was originally proposed by Olley, G.S. and Pakes, A. (1996)
<doi:10.2307/2171831>. The second by Levinsohn, J. and Petrin, A. (2003)
<doi:10.1111/1467-937X.00246>. And the third by Wooldridge (2009)
<doi.org/10.1016/j.econlet.2009.04.026>.

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
