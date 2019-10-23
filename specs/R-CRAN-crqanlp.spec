%global packname  crqanlp
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          1%{?dist}
Summary:          Cross-Recurrence Quantification Analysis for Dynamic NaturalLanguage Processing

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-crqa 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-corpus 
BuildRequires:    R-CRAN-gutenbergr 
BuildRequires:    R-CRAN-RCurl 
Requires:         R-CRAN-crqa 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-corpus 
Requires:         R-CRAN-gutenbergr 
Requires:         R-CRAN-RCurl 

%description
Cross-recurrence quantification analysis for word series, from text, known
as categorical recurrence analysis. Uses the 'crqa' R package by Coco and
Dale (2014) <doi:10.3389/fpsyg.2014.00510>. Functions are wrappers to
facilitate exploration of the sequential properties of text.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
