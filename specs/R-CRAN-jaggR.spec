%global packname  jaggR
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Supporting Files and Functions for the Book Bayesian Modellingwith 'JAGS'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-formatR 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-formatR 
Requires:         R-CRAN-glue 
Requires:         R-graphics 
Requires:         R-stats 

%description
All the data and functions used to produce the book. We do not expect most
people to use the package for any other reason than to get simple access
to the 'JAGS' model files, the data, and perhaps run some of the simple
examples. The authors of the book are David Lucy (now sadly deceased) and
James Curran. It is anticipated that a manuscript will be provided to
Taylor and Francis around February 2020, with bibliographic details to
follow at that point. Until such time, further information can be obtained
by emailing James Curran.

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
%doc %{rlibdir}/%{packname}/models
%{rlibdir}/%{packname}/INDEX
