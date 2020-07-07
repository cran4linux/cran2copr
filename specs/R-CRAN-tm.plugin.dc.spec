%global packname  tm.plugin.dc
%global packver   0.2-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.8
Release:          3%{?dist}
Summary:          Text Mining Distributed Corpus Plug-In

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tm >= 0.6
BuildRequires:    R-CRAN-DSL >= 0.1.3
BuildRequires:    R-CRAN-slam >= 0.1.22
BuildRequires:    R-CRAN-NLP 
BuildRequires:    R-utils 
Requires:         R-CRAN-tm >= 0.6
Requires:         R-CRAN-DSL >= 0.1.3
Requires:         R-CRAN-slam >= 0.1.22
Requires:         R-CRAN-NLP 
Requires:         R-utils 

%description
A plug-in for the text mining framework tm to support text mining in a
distributed way. The package provides a convenient interface for handling
distributed corpus objects based on distributed list objects.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
