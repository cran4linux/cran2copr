%global packname  DMwR2
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Functions and Data for the Second Edition of "Data Mining withR"

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-class >= 7.3.14
BuildRequires:    R-rpart >= 4.1.10
BuildRequires:    R-CRAN-zoo >= 1.7.10
BuildRequires:    R-CRAN-readr >= 1.0.0
BuildRequires:    R-CRAN-xts >= 0.9.7
BuildRequires:    R-CRAN-DBI >= 0.5
BuildRequires:    R-CRAN-quantmod >= 0.4.5
BuildRequires:    R-CRAN-dplyr >= 0.4.3
BuildRequires:    R-methods 
Requires:         R-class >= 7.3.14
Requires:         R-rpart >= 4.1.10
Requires:         R-CRAN-zoo >= 1.7.10
Requires:         R-CRAN-readr >= 1.0.0
Requires:         R-CRAN-xts >= 0.9.7
Requires:         R-CRAN-DBI >= 0.5
Requires:         R-CRAN-quantmod >= 0.4.5
Requires:         R-CRAN-dplyr >= 0.4.3
Requires:         R-methods 

%description
Functions and data accompanying the second edition of the book "Data
Mining with R, learning with case studies" by Luis Torgo, published by CRC
Press.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
