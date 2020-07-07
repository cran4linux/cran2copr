%global packname  rtext
%global packver   0.1.21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.21
Release:          3%{?dist}
Summary:          R6 Objects for Text and Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-R6 >= 2.1.2
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-RSQLite >= 1.0.0
BuildRequires:    R-CRAN-digest >= 0.6.9
BuildRequires:    R-CRAN-Rcpp >= 0.12.5
BuildRequires:    R-CRAN-stringb >= 0.1.13
BuildRequires:    R-CRAN-hellno >= 0.0.1
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-R6 >= 2.1.2
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-RSQLite >= 1.0.0
Requires:         R-CRAN-digest >= 0.6.9
Requires:         R-CRAN-Rcpp >= 0.12.5
Requires:         R-CRAN-stringb >= 0.1.13
Requires:         R-CRAN-hellno >= 0.0.1
Requires:         R-stats 
Requires:         R-graphics 

%description
For natural language processing and analysis of qualitative text coding
structures which provide a way to bind together text and text data are
fundamental. The package provides such a structure and accompanying
methods in form of R6 objects. The 'rtext' class allows for text handling
and text coding (character or regex based) including data updates on text
transformations as well as aggregation on various levels. Furthermore, the
usage of R6 enables inheritance and passing by reference which should
enable 'rtext' instances to be used as back-end for R based graphical text
editors or text coding GUIs.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/testfiles
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
