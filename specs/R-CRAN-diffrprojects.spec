%global packname  diffrprojects
%global packver   0.1.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.14
Release:          3%{?dist}
Summary:          Projects for Text Version Comparison and Analytics in R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-R6 >= 2.1.2
BuildRequires:    R-CRAN-RSQLite >= 1.0.0
BuildRequires:    R-CRAN-stringdist >= 0.9.4.1
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.6
BuildRequires:    R-CRAN-rtext >= 0.1.20
BuildRequires:    R-CRAN-stringb >= 0.1.13
BuildRequires:    R-CRAN-hellno >= 0.0.1
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-stats 
Requires:         R-CRAN-R6 >= 2.1.2
Requires:         R-CRAN-RSQLite >= 1.0.0
Requires:         R-CRAN-stringdist >= 0.9.4.1
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-Rcpp >= 0.12.6
Requires:         R-CRAN-rtext >= 0.1.20
Requires:         R-CRAN-stringb >= 0.1.13
Requires:         R-CRAN-hellno >= 0.0.1
Requires:         R-CRAN-magrittr 
Requires:         R-stats 

%description
Provides data structures and methods for measuring, coding, and analysing
text within text corpora. The package allows for manual as well computer
aided coding on character, token and text pair level.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/testfiles
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
