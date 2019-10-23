%global packname  SCCS
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          The Self-Controlled Case Series Method

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-dummies 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-R.methodsS3 
BuildRequires:    R-CRAN-gnm 
Requires:         R-survival 
Requires:         R-splines 
Requires:         R-CRAN-dummies 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-R.methodsS3 
Requires:         R-CRAN-gnm 

%description
Various self-controlled case series models used to investigate
associations between time-varying exposures such as vaccines or other
drugs or non drug exposures and an adverse event can be fitted. Detailed
information on the self-controlled case series method and its extensions
with more examples can be found in Farrington, P., Whitaker, H., and
Ghebremichael Weldeselassie, Y. (2018, ISBN: 978-1-4987-8159-6.
Self-controlled Case Series studies: A modelling Guide with R. Boca Raton:
Chapman & Hall/CRC Press) and <https://sccs-studies.info>.

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
