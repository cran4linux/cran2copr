%global packname  SP2000
%global packver   0.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}
Summary:          'Catalogue of Life China' Toolkit

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-pbmcapply 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlist 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-pbmcapply 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlist 

%description
A programmatic interface to <http://sp2000.org.cn>, re-written based on an
accompanying 'Species 2000' API. Access tables describing catalogue of the
Chinese known species of animals, plants, fungi, micro-organisms, and
more. The development of 'SP2000' package was supported by Yunnan
University's Research Innovation Fund for Graduate Students.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/htmlwidgets
%{rlibdir}/%{packname}/INDEX
