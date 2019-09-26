%global packname  newsmap
%global packver   0.6.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.9
Release:          1%{?dist}
Summary:          Semi-Supervised Model for Geographical Document Classification

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quanteda > 1.4
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-quanteda > 1.4
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-Matrix 
Requires:         R-CRAN-stringi 

%description
Semi-supervised model for geographical document classification (Watanabe
2018) <doi:10.1080/21670811.2017.1293487>. This package currently contains
seed dictionaries in English, German, French, Spanish, Japanese, Russian
and Chinese (Simplified and Traditional).

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
