%global packname  vcd
%global packver   1.4-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.4
Release:          1%{?dist}
Summary:          Visualizing Categorical Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.4.0
Requires:         R-core >= 2.4.0
BuildArch:        noarch
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-MASS 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-lmtest 
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-MASS 
Requires:         R-grDevices 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-lmtest 

%description
Visualization techniques, data sets, summary and inference procedures
aimed particularly at categorical data. Special emphasis is given to
highly extensible grid graphics. The package was package was originally
inspired by the book "Visualizing Categorical Data" by Michael Friendly
and is now the main support package for a new book, "Discrete Data
Analysis with R" by Michael Friendly and David Meyer (2015).

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
