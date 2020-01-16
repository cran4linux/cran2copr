%global packname  qCBA
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          1%{?dist}
Summary:          Quantitative Classification by Association Rules

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 2.7.0
Requires:         R-core >= 2.7.0
BuildArch:        noarch
BuildRequires:    R-CRAN-arc >= 1.1
BuildRequires:    R-CRAN-rJava >= 0.5.0
BuildRequires:    R-CRAN-arules 
BuildRequires:    R-methods 
Requires:         R-CRAN-arc >= 1.1
Requires:         R-CRAN-rJava >= 0.5.0
Requires:         R-CRAN-arules 
Requires:         R-methods 

%description
CBA postprocessing algorithm that creates smaller models for datasets
containing quantitative (numerical) attributes. Article describing QCBA is
published in Tomas Kliegr (2017) <arXiv:1711.10166>.

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
%doc %{rlibdir}/%{packname}/java
%{rlibdir}/%{packname}/INDEX
