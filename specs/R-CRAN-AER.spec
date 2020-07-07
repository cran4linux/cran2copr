%global packname  AER
%global packver   1.2-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.9
Release:          3%{?dist}
Summary:          Applied Econometrics with R

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sandwich >= 2.4.0
BuildRequires:    R-survival >= 2.37.5
BuildRequires:    R-CRAN-car >= 2.0.19
BuildRequires:    R-CRAN-Formula >= 0.2.0
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-stats 
Requires:         R-CRAN-sandwich >= 2.4.0
Requires:         R-survival >= 2.37.5
Requires:         R-CRAN-car >= 2.0.19
Requires:         R-CRAN-Formula >= 0.2.0
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-zoo 
Requires:         R-stats 

%description
Functions, data sets, examples, demos, and vignettes for the book
Christian Kleiber and Achim Zeileis (2008), Applied Econometrics with R,
Springer-Verlag, New York. ISBN 978-0-387-77316-2. (See the vignette "AER"
for a package overview.)

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
