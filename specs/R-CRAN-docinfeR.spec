%global packname  docinfeR
%global packver   2020.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2020.1.0
Release:          2%{?dist}%{?buildtag}
Summary:          Automatic Reporter for Inference Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-tictoc 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-tictoc 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-Rdpack 

%description
Generation of a document (.docx file) with inference analysis reporting of
a selected dataset. REFERENCE: R. Sarmento, V. Costa (2017)
<DOI:10.4018/978-1-68318-016-6>.

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
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
