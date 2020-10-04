%global packname  DMwR
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          3%{?dist}%{?buildtag}
Summary:          Functions and data for "Data Mining with R"

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-class >= 7.3.1
BuildRequires:    R-rpart >= 3.1.46
BuildRequires:    R-grid >= 2.10.1
BuildRequires:    R-CRAN-zoo >= 1.6.4
BuildRequires:    R-CRAN-abind >= 1.1.0
BuildRequires:    R-CRAN-ROCR >= 1.0
BuildRequires:    R-CRAN-xts >= 0.6.7
BuildRequires:    R-CRAN-quantmod >= 0.3.8
BuildRequires:    R-lattice >= 0.18.3
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
Requires:         R-class >= 7.3.1
Requires:         R-rpart >= 3.1.46
Requires:         R-grid >= 2.10.1
Requires:         R-CRAN-zoo >= 1.6.4
Requires:         R-CRAN-abind >= 1.1.0
Requires:         R-CRAN-ROCR >= 1.0
Requires:         R-CRAN-xts >= 0.6.7
Requires:         R-CRAN-quantmod >= 0.3.8
Requires:         R-lattice >= 0.18.3
Requires:         R-methods 
Requires:         R-graphics 

%description
This package includes functions and data accompanying the book "Data
Mining with R, learning with case studies" by Luis Torgo, CRC Press 2010.

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
